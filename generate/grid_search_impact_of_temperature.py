
import subprocess
from datetime import datetime

now = datetime.now()

DEBUG = False
PROBLEMS = [78]
# It appears that beam search only ever does one rollout, so if we want to rerun
# the beam search then we need to run the script multiple times.
BEAM_SEARCH_ROLLOUTS = 100

for temperature in [ 1 / 1.6180339887498547 ** i for i in range(1, 11, 2)]:
    for problem in PROBLEMS:
        output_directory = f"results/do-prompts-matter{{model=code-davinci-002,prompt=default,temp={round(temperature, 3)}]}}"
        if DEBUG:
            print(output_directory)
            continue
        for index in range(0, BEAM_SEARCH_ROLLOUTS):
            output = subprocess.run(([
                "python", "synthesis_exp.py",
                "-i", str(problem),
                "-l", "code-davinci-002",
                "--alg", "bs",
                "--num-beams", "2",
                "--temperature", str(temperature),
                "--save", output_directory,
                "--prefix", f"candidate={index},",
            ]))