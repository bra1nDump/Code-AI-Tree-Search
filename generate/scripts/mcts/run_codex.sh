 # don't plan to run too many samples, show the advantage of a small sample size is okay
 python synthesis_exp.py -s 4000 -e 4100 -l code-davinci-002 --max-sample-times 128 --rollout 4 --time-limit 7200 --save codex_results --prefix codex2-4- --debug

 # --alg mcts-multi 