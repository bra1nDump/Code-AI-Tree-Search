import numpy as np
import pandas as pd
import json
import seaborn
import matplotlib.pyplot as plt
import glob
from collections import defaultdict
import itertools
import typing

import matplotlib.pyplot as plt

buckets = defaultdict(int)
bucket_by_test_case = defaultdict(int)

# Observation: 
# The dimensions of the graph don't correspond to the dimensions of the data
# Usually the data is flattened out by the dimensionality of the subplots.
# The data also contains another dimension for the FacetGrid, which in our case are temperature (column) and later prompt (row)


# The structure is as follows:
# Program 1, Temperature 1;  Program 2, Temperature 1;  ...; Program 1, Temperature 2;  Program 2, Temperature 2; ...

# The following arrays are aligned with each other:
# Test cases solved by 1, 1; Test cases solved by 2, 1; ...; Test cases solved by 1, 2; Test cases solved by 2, 2; ...
# Temperature 1;             Temperature 1;             ...; Temperature 2;             Temperature 2; ...
total_tests_passed_by_program = []
temperatures_by_program = []

# Found this here https://stackoverflow.com/questions/41471238/how-to-make-heatmap-square-in-seaborn-facetgrid
# temperatures = 5
# test_cases = 5
# programs = 5

# indices = pd.MultiIndex.from_product((range(temperatures), range(test_cases), range(programs)), names=('temperature', 'test case', 'program'))
# data = pd.DataFrame(np.random.uniform(0, 100, size=len(indices)), index=indices, columns=('value',)).reset_index()
# print(indices)
# print(data)

# def draw_heatmap(*args, **kwargs):
#     data = kwargs.pop('data')
#     d = data.pivot(index=args[1], columns=args[0], values=args[2])
#     sns.heatmap(d, **kwargs)

figure, axes = plt.subplots(5, 1)
# Increase default figure size
figure.set_size_inches(18.5, 18.5)

for temperature_index, temperature in enumerate(["0.618", "0.236", "0.034", "0.09", "0.013"]):
    files = glob.glob(f"../generate/results/do-prompts-matter{{model=code-davinci-002,prompt=default,temp={temperature}]}}/*.result.json")
    width_guess = 0

    program_by_test_case: typing.List[typing.List[bool]] = []

    # Each file corresponds to a single program that was generated in case of beam search
    # For MCTS it would be multiple programs per file.
    for filename in files:
        with open(filename, "r") as f: 
            results = json.load(f)
            # We can always take the first element of the list because the beam
            # search algorithm only has one rollout.
            passing_tests = results["train_rewards"][0]
            width_guess = max(width_guess, len(passing_tests))

            for i, maybe_passed in enumerate(passing_tests):
                if maybe_passed:
                    bucket_by_test_case[i] += 1

            tests_passed_by_program = sum(passing_tests)
            total_tests_passed_by_program.append(tests_passed_by_program)
            temperatures_by_program.append(temperature)

            program_by_test_case.append(passing_tests)

    
    # Normalize the lists (so that they are all the same length), remember compliation erros and runtime erros
    # have lists of length 0 for test cases solved.
    normalized_program_by_test_case = list(itertools.zip_longest(*program_by_test_case, fillvalue=False))
    np_normalized_program_by_test_case = np.array(normalized_program_by_test_case)

    # Sort the rows by the number of test cases each program solves.
    np_normalized_program_by_test_case = np_normalized_program_by_test_case[np.argsort(np.sum(np_normalized_program_by_test_case, axis=1))[::-1]]

    # Sort the columns by the number of programs that solve each test case.
    np_normalized_program_by_test_case = np_normalized_program_by_test_case[:, np.argsort(np.sum(np_normalized_program_by_test_case, axis=0))[::-1]]

    # Filter out the programs (rows) that solve no test cases.
    # np_normalized_program_by_test_case = np_normalized_program_by_test_case[np.sum(np_normalized_program_by_test_case, axis=1) > 0]

    # Plot the heatmap by appending to the current plot.

    # plt.figure(figsize=(20, 20))
    axes[temperature_index].set_title(f'Temperature: {temperature}')
    seaborn.heatmap(np_normalized_program_by_test_case, cmap="YlGnBu", ax=axes[temperature_index])

    # print(np_normalized_program_by_test_case)

    # test_stats_by_program.extend(list(np_normalized_program_by_test_case))
    # temperatures_by_program_2.extend([temperature] * len(np_normalized_program_by_test_case))

# Plot the heatmap first
# heatmap_data = np.array(test_stats_by_program)
# temperatures_for_each_heatmap = np.array(temperatures_by_program_2)
# print(heatmap_data)
# print(temperatures_for_each_heatmap)
# df = pd.DataFrame(dict(heatmap_data=heatmap_data, temperatures_for_each_heatmap=temperatures_for_each_heatmap))

# seaborn.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
# g = seaborn.FacetGrid(df, col="temperatures_for_each_heatmap", aspect=15, height=0.5, palette="tab20c")
# g.map(seaborn.heatmap, "heatmap_data", linewidths=0.05, linecolor="white", cbar=False, vmin=0, vmax=1)

# Save all temperatures to a single file, clear the plot
plt.savefig("special-test-cases.png")
plt.clf()

total_tests_passed_by_program = np.array(total_tests_passed_by_program)
g = np.array(temperatures_by_program)
df = pd.DataFrame(dict(x=total_tests_passed_by_program, g=g))
print(df)


# https://seaborn.pydata.org/examples/kde_ridgeplot.html
seaborn.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# Initialize the FacetGrid object
pal = seaborn.cubehelix_palette(5, rot=-.25, light=.7)
g = seaborn.FacetGrid(df, row="g", hue="g", aspect=15, height=0.5, palette=pal)

# Draw the densities in a few steps
g.map(seaborn.kdeplot, "x",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=1.5)
g.map(seaborn.kdeplot, "x", clip_on=False, color="w", lw=2, bw_adjust=.5)

# passing color=None to refline() uses the hue mapping
g.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)

# Define and use a simple function to label the plot in axes coordinates
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)

g.map(label, "x")

# Set the subplots to overlap
g.figure.subplots_adjust(hspace=-.25)

# Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[], ylabel="")
g.despine(bottom=True, left=True)

plt.savefig('temparature-and-total-tests-solved.png')


exit(1)

# Load the example flights dataset and convert to long-form
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)

plt.show()