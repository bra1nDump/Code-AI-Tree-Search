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

from dataclasses import dataclass

@dataclass
class Observation:
    temperature: float
    # prompt: str
    programIndex: int
    
# Observations need to be sorted - so the indexes of the programs that actually show up 
# will be different from the index of the original program.
# TODO: Replace the indexes of programss in the graph by the original indexes to look them up.
# Two maps:
# originalProgramIndex -> new, originalTestCaseIndex -> new
# Sort test cases and programs using numpy.argsort, they will give us the mapping that we 
# can use to sort and later lookup

# Can we sort the observations? So the final structure?

observations: typing.List[Observation] = []

# I don't think we need this - we can just ommit the tests that are empty, they are not 
# observations. We want "tidy-long form" data https://tinyurl.com/2ktdm9mf
def pad_lists(input_list, default_value):
    max_length = max(len(inner_list) for inner_list in input_list)
    result = [inner_list + [default_value] * (max_length - len(inner_list)) for inner_list in input_list]
    return result

total_tests_passed_by_program = []
temperatures_by_program = []

temperature_by_program_by_test_cases = []

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

            program_by_test_case.append(passing_tests)
            
    # Normalize the lists (so that they are all the same length), remember compliation erros and runtime erros
    # have lists of length 0 for test cases solved.
    temperature_by_program_by_test_cases.append(pad_lists(program_by_test_case, False))
    

# Make it a numpy array so that we can use numpy functions on it
temperature_program_tests = np.array(temperature_by_program_by_test_cases)

# Sort the test cases by how many programs pass them
how_many_programs_pass_a_test_across_all_temperatures = np.sum(temperature_program_tests, axis=(0, 1))
test_axis_order = np.argsort(how_many_programs_pass_a_test_across_all_temperatures)
test_axis_order_reversed = np.argsort(how_many_programs_pass_a_test_across_all_temperatures)[::-1]
sorted_tests = np.take_along_axis(temperature_program_tests, test_axis_order_reversed[np.newaxis, np.newaxis, :], axis=2)

# Sort the programs by how many test cases they pass
how_many_test_cases_does_a_given_program_pass = np.sum(sorted_tests, axis=2)
program_axis_order = np.argsort(how_many_test_cases_does_a_given_program_pass, axis=1)
program_axis_order_descending = program_axis_order[:, ::-1]

# Observation:
# The order array returned could have 2 encodings, which I mixed up:
# Correct: [0, 40, 3, ...], means that element at index 40 from the original array goes to index 1 in the new array.
# Wrong: Element at index 1 in the old array goes to index 40 in the new array
# I suggest experimenting with smaller arrays to verify assumptions.

# Advanced indexing from chat gpt 4 https://shareg.pt/iElyy4R
sorted_tests_and_program = sorted_tests[np.arange(sorted_tests.shape[0])[:, np.newaxis], program_axis_order_descending]



# Save all temperatures to a single file, clear the plot
plt.savefig("special-test-cases.png")
plt.clf()

total_tests_passed_by_program = np.array(total_tests_passed_by_program)
g = np.array(temperatures_by_program)
df = pd.DataFrame(dict(x=total_tests_passed_by_program, g=g))
pd.DataFrame()
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