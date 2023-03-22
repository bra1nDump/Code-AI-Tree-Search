# Resources

- Main website https://codeaimcts.github.io/
- Github https://github.com/shunzh/Code-AI-Tree-Search
- Paper PDF https://openreview.net/pdf?id=Lr8cOOtYbfL
- Open review https://openreview.net/forum?id=Lr8cOOtYbfL
- Rent GPUs https://brev.dev/

# Wednesday 15

## Numpy, take_along_axis

The learing is that take_along_axis reorders the array along the given axis.
As the indexes it needs the same shaped array as the input array.
The indexes need to be the same shape as the input array, because each element can be shifted to a new location.

For example

```python
[[0, 1],
 [2, 3]]

# To reorder columns we need
[[1, 0],
 [1, 0]]

# For this case we don't need the outer dimension so we can use np.newaxis
[1, 0][np.newaxis, :]
# produces
[[1, 0]]

# [,] notation means adding a new axis, its a numpy thing, not python
```

```python
>>> a = np.array([[[0, 1], [0, 0]], [[1, 1], [1, 0] ] ])
array([[[0, 1],
        [0, 0]],

       [[1, 1],
        [1, 0]]])
>>> s = np.take_along_axis(a, np.array([ [1, 0], [1, 0] ])[:, None], axis=1)
>>> s
array([[[0, 1]],

       [[1, 1]]])
>>> s = np.take_along_axis(a, np.array([ [1, 0], [1, 0] ])[None, :], axis=1)
>>> a
array([[[0, 1],
        [0, 0]],

       [[1, 1],
        [1, 0]]])
```

### Log

Found this here https://stackoverflow.com/questions/41471238/how-to-make-heatmap-square-in-seaborn-facetgrid

The dimensions of the graph don't correspond to the dimensions of the data
Usually the data is flattened out by the dimensionality of the subplots.
The data also contains another dimension for the FacetGrid, which in our case are temperature (column) and later prompt (row)

The structure is as follows:
Program 1, Temperature 1; Program 2, Temperature 1; ...; Program 1, Temperature 2; Program 2, Temperature 2; ...

The following arrays are aligned with each other:
Test cases solved by 1, 1; Test cases solved by 2, 1; ...; Test cases solved by 1, 2; Test cases solved by 2, 2; ...
Temperature 1; Temperature 1; ...; Temperature 2; Temperature 2; ...

I don't think we need this - we can just ommit the tests that are empty, they are not
observations. We want "tidy-long form" data https://tinyurl.com/2ktdm9mf

# Try next

- Start writing what we did?
- Do they have temperature for gpt2? Try running their models with the higher temperature.
- [ploting] Add if the test case failed with wrong output vs runtime error - different color
  - [optional] Additionally classify the runtime errors

## Prompt engineering

- Give more examples - see how many it needs to pass all
  - Give it the ones it failed on, can it pass them now?
  - Give all examples - easier. Best case.
- Redo the prompt copletely - change the content, give different examples (generate?)

## Good prefix

- We can play with the temperature once we find a good prefix (rollout) with a high temperature. We want some creativity to stear the model, but we don't want the
- Shorten the perfect solution and see if it complete it
  - Shorten by AST node
  - Splitting by certainty of the string, find equal split points

## Token count

- Fixed
- AST
- Uncertanty

## Tools

- Loom - researches are using it to visualize the tree

TOP PRIORITY
Open the file with the plot in vscode and just keep it open lol

# Plotting

I can't seem to create multi dimensional np array dataframes, hmm
Maybe just skip the dataframe?

## Prompt experimentation

The main idea is to completely redo the problem statement, examples and even replace input with call based problems.

What this gives us:

- Understanding if the problem is already in the train data set. For example if we rephrase it slightly and it can't do as good or doesnt pick the right algorithm - most likely the model is memorizing.
- Removing input parsing and suggesting to "complete this function" can get us better results because the model has less thrings to pay attention to.
- Try shortening the problem
- Try explaining why a certain sample test input output produce the given result
- Try ommmiting Polycarp stuff (so preabmle english ) and just giving the raw requirements and examples
- Variations of the above

## Tools?

Can we figure out what is the model paying attention to in the prompt? Any tools for this?
Only public models tho.
LLaMA, but it sucks at coding :

We have been working with APPS, maybe look for other datasets how they form the examples. Usually some explanation of the test cases is given. I rely on it quite a bit when understanding the problem myself.

<!--
- Prompt eng with beam, different prefix for the output to keep the old results to measure
  - Depending on how this goes try with MCTS
  - GPT2 will suck, they definetely tried at leas -->

## Locally

- Check the paper for what k they tested

- [2 days?, depending on setup] Multiple tokens at a time, once we generated a string - it has no idea how many tokens produced it
  - Find all the locations where we sample from the transformer
- Probability with --debug will show the tokens per node so easy to test

- [2 day effort + ] Enough tokens to satisfy tree sitter (successful parse)'

# Saturday 11

## Plan

run --temperature 0.7 --problem 78 --prefix problem --rollouts 10

- Read the problem
- Run codex rollout times
  - Save each code in a separate file /problem_78/rollout_1/code.py results/78.code.1.py
  - Evaluate each run and score it, store in a separate file /problem_78/rollout_1/stats.json

plot --problem 78

Reads the stats and plots it magically

## Log

Trying codex2
Number of rollouts is crazy high, 2k, long wait time and expensive (lets check the pricing for model 2)

mcts-multi keeps breaking - suggests they found this not promising and didn't run the final benchmarks on it.

Last breakage:

```log
Traceback (most recent call last):
  File "synthesis_exp.py", line 289, in <module>
    main()
  File "synthesis_exp.py", line 173, in main
    states, info = uct_multistep_exp(args, env, dp, log_loc, start)
  File "/Users/kirilldubovitskiy/projects/Code-AI-Tree-Search/generate/uct.py", line 141, in uct_multistep_exp
    raise e
  File "/Users/kirilldubovitskiy/projects/Code-AI-Tree-Search/generate/uct.py", line 127, in uct_multistep_exp
    plot_tree(agent.root, env, log_loc)
  File "/Users/kirilldubovitskiy/projects/Code-AI-Tree-Search/generate/../dyna_gym/agents/mcts.py", line 330, in plot_tree
    pos = hierarchy_pos(G, root=root.id)
  File "/Users/kirilldubovitskiy/projects/Code-AI-Tree-Search/generate/../eval/utils.py", line 103, in hierarchy_pos
    raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')
TypeError: cannot use hierarchy_pos on a graph that is not a tree
```

Results are not being written out
Codex 2 is the most capable model ....??

What makes the score of 0?
Is this compilation errors?
If we feed the prompt with the previous error

- Try codex3 - same as codex2
  - Prompt eng with beam, different prefix for the output to keep the old results to measure
    - Depending on how this goes try with MCTS
    - GPT2 will suck, they definetely tried at leas

78 gpt2 failed, codex2 succeeds

Ideas:

- Prompt format - clean the data, dollar signs, ===== question =====
  - We need some stable set of problems to test against
  - Is there a tool for this?
    - Capturing one run of the program - copy some directory with tmp output in a secret location? Like Jupiter notebook
    - This would be useful for iterating
- Better print out the directory structure - no python in json format
- Immutable log of runs - to avoid overriding stuff

Shotgun approach is few evaluations on many problems - not great.
See a distribution of scores for a single problem. If there is a clear curve we can predict how many runs we need to pass 0.9 score 0.7 etc.

We want to try multiple temperatures.

What can we write up publish goal - Wednsday.
Comment on open review.

For higher temperatures it is more likely to generate a solution to a non-trivial problem, or at least go into the right direrction.

# Thursday 9

No prompt eng at all?
Lets check the code

Assert

We have questions with score of 0, what is so special about those questions?

Was gpt2 trained on the same apps dataset????
How they ensured its not?

We have no idea how to give a prompt. We have not found good onese.
Specifically for code sytnthesis. - value added there.
We can find good prompts in papers? or just experiment with them.

We run N prompts and see which prompts do better.

Try the seed, codex wont need this.

# Wednesday 8

[Key] `python synthesis_exp.py -i 8 --alg bs --debug`
`-s start -e end`

We have no idea how codex was trained.
What model was used again? Was it GPT-2 codex? so codex2?

I assume codex already has bias towards "good" code.
[Hypothsis] This monte carlo appraoch was tried with codex-3 or even-2 it would not make a difference because codex already has bias towards "good" code.

Another optimization we can make is instead of top_k for only the next token we can get top_k for the next D tokens.
This will introduce the "batch" idea. We can now explore a larger tree (will account for more of the final program compared to the current approach).

Ideally we want D to be dynamic - so it would generate meaningful pieces of code.
Simple batch idea: new line!
No need to complicate things.

So they are running it with codex 2
see run_codex script

## Dev machine hosting

### Brev - rented, tried, working :D

### Github codespaes, tried, super slow to download, requested GPU, not default

Seems I am not using GPU on Brev

```bash
$ python synthesis_exp.py -i 4136 --alg sample --num-samples 16 --prefix s-

final program:
# cook your dish here
a,b = map(int,input().split())
print(a+b)

train reward 1.0
test reward 1.0
time elapsed 142.14831113815308
sample times 16
```

Failed with max token exceoption.
Might have something to do with the GPU memory, or configuration. Will try to repro and take note of this.

```log
Solving Problem #9
Token indices sequence length is longer than the specified maximum sequence length for this model (1052 > 1024). Running this sequence through the model will result in indexing errors
Input length of input_ids is 1052, but `max_length` is set to 1024. This can lead to unexpected behavior. You should consider increasing `max_new_tokens`.
```

Found max_lengt=1024 in the generate_gpt_codes
Same as horizon

Increased horizon to 2048

```log
(py38) ml-env ➜  generate git:(main) ✗ ./scripts/beam/run.sh --debug
./scripts/beam/run.sh: 1: ./scripts/basis.sh: Permission denied
{'alg': 'bs',
 'arch': 'gpt2',
 'dataset': 'apps',
 'debug': False,
 'device': device(type='cuda'),
 'early_stop': False,
 'end': 5000,
 'entropy_weighted_strategy': 'none',
 'horizon': 2048,
 'index': None,
 'indices': None,
 'load': '../models/1.5B',
 'load_value': None,
 'max_sample_times': 768,
 'new_token_num': None,
 'no_cuda': False,
 'no_prompt_cache': False,
 'no_seq_cache': False,
 'num_beams': 1,
 'num_samples': 1,
 'overfit': False,
 'peek': False,
 'prefix': '',
 'public_cases': 'half',
 'rerun': False,
 'rollout': 1,
 'save': './results',
 'seed': 0,
 'start': 0,
 'task': 'gen_code',
 'test_all_beams': False,
 'test_loc': '../data_split/test.json',
 'time_limit': 10000,
 'top_k_cache_steps': 1024,
 'ts_mode': 'best',
 'ucb_base': 10.0,
 'ucb_constant': 4.0,
 'uct_alg': 'var_p_uct',
 'width': 3}
Loading model ../models/1.5B
Model loaded/initialized.
Found ./results/0.json, args.rerun not enabled, skipping
Found ./results/1.json, args.rerun not enabled, skipping
Found ./results/2.json, args.rerun not enabled, skipping
Found ./results/3.json, args.rerun not enabled, skipping
Found ./results/4.json, args.rerun not enabled, skipping
Found ./results/5.json, args.rerun not enabled, skipping
Found ./results/6.json, args.rerun not enabled, skipping
Found ./results/7.json, args.rerun not enabled, skipping
Found ./results/8.json, args.rerun not enabled, skipping
Solving Problem #9
Token indices sequence length is longer than the specified maximum sequence length for this model (1052 > 1024). Running this sequence through the model will result in indexing errors
```

Issue in transformers library.
Used by GPT2, lets try Neo

9 has the problem
51
So I think the problem is the problem text is too big. I think max_new_tokens is defined by the size of the GPU because I am running the same code as the paper.

Potentially coming from here tokenizer = transformers.AutoTokenizer.from_pretrained('gpt2')

To check I can test tokenizer on the problem text.

Would be nice to attach debugger.

Trying to reduce number of tokens.

Noticed 51 text is russian. Hmm, maybe takes more tokens to encode?

GPT does not support these many tokens? https://news.ycombinator.com/item?id=22197774
Makes sense I guess, the output can't be jsut 'scaled up'

Lets try NEO

Decreasing words in problem worked

I am thinking increasing horizon backfired?

To load a given model - neo="-l ../models/2.7B" for example

python synthesis_exp_smc.py -i 51 has a better error code and does not crash :D
[Opportunity] Fix the error on the smc less code

Nice, okay so seems like fitness is how likely is this branch resulting in a good program.

Neo also is also gpt2, so same issue with context length. Makes sense that some programs just straignt up fail because of the window size.

Brev - code killed, seems out of memory. Loaded Neo model. Only 15 gb on this machine.

Bash command to get gpu memory usage
[Nice] `watch -n 1 nvidia-smi`
7gb used for 1.5 B model

I see so RAM 16 runs out :D

## Speed

`python synthesis_exp.py -i 50 --rerun --alg bs -l ../models/1.5B`
So running 1.5 locally to gen one program - 8.784324645996094, 7 with GPU
No GPU --no-cuda 57.82056164741516
6x times

Running locally on mac, 1.5 also program 50
66.86661410331726

Conclusion - I really don't need the GPU while writing the logic for this, only when testing.
For testing a single g4da.xlarge is not enough. Lets try with another instance later, or maybe adding more memory. Also most likely I need a cluster instead of adding more memory to one to run the benchmarks.

eluther need man power have compute :?
Grant?

# Tuesday 7

Some solutions are better.
In the training data all programms are the same - worse code is treated the same as good code.
Can we bias the model to generate cooler code? Filter, map, all etc.

They don't have a learned function for P_UCB, just like alpha go.

# Monday 6

PG-TD
Planning-Guided Transformer-Decoding

Where are they getting the public test cases

AlphaCode?
Sample complete programs against test cases, who passes more tests wins.

I see, so when generating code the tests are not considered.

"Ideal code generation algorithm shold stop early" - suggests that tasks are partial
How does it test that?

Lookahead search?
Tokens that will lead to high-quality codes

Planner + transofmer beam search

"Specifically, the Transformer beam search
algorithm and the next-token probabilities are used inside the planner to provide useful heuristics.
We find that a straightforward integration between the planner and the Transformer can be computationally inefficient"
Which seems like what we are currently doing.
How inefficient is it?

Can use any transformer as the code gen backbone.

They change the reward function of the planner without updating the transformer.

RL - reinforcement learning, punishing for making mistakes.
Deep learning is different?

We can partially compile.

AlphaGo - plays go, monte carlo tree search.
Play out the game completely see which moves leads to more victories statistically.

Markov Decision Process - MDP

Instead of optimising for text completion - so optimizing for next token they optimize for passing the tests - which means its a better program.

state is the problem description + code generated so far. Pass rate is the reward for a given state.

Markov Decision Process needs an optimal policy. In this case its inspired by Monte-Carlo tree search.

The chain is basically a tree. Each node is an action - which is the next token generated by the transformer.

Somehow we know which branch to take.

Max rollouts - total steps we will take.

When picking the beam winners across the children, should we bias the children.

Add incremental parsing to know where we are and if we have a syntax error - abort.

Restating algorithm with my own words:

- For total number of steps we are willing to take (total number of programs generated)
- Every roll out we will add new children
-

They can try exploiting the 'best' tokens?

c - how often explore less visited states

The beam is very deep compared to the depth of the tree used in monte carlo tree search.
This paper seems to limit to short programs, otherwise its not better than sampling at all.

Improvement ideas:

- Use monte carlo only on important nodes - for example function signatures
- Beam chunks of code - stop once the body is generated, continue monte carlo from there.

No code
Say nothing about how the rewards do

Dick around with the prompt
1% point improvement is what this paper achieves. Can we get that with just the prompt.

See if we can run the model with a custom prompt.
