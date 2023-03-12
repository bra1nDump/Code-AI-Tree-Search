import multiprocessing
from typing import Tuple, List

import testing_util as test_util
import numpy as np

COMPILE_ERROR = -2
RUNTIME_ERROR = -1

"""
Running set in a separate process
https://github.com/hendrycks/apps/blob/83d925041b1c43c32b56d444bb315f729f4ff633/eval/test_one_solution.py#L57
"""
def _temp_run(prob_path, output_str, mode, public_test_cases, result):
    result.append(test_util.run_test(prob_path=prob_path, candidate_program=output_str, mode=mode, public_test_cases=public_test_cases))

def check_correctness(prob_path, output_str, mode, public_test_cases):
    """Check correctness of code generation with a global timeout.
    The global timeout is to catch some extreme/rare cases not handled by the timeouts
    inside `run_test`"""
    manager = multiprocessing.Manager()
    result = manager.list()
    p = multiprocessing.Process(target=_temp_run, args=(prob_path, output_str, mode, public_test_cases, result))
    p.start()
    p.join(timeout=10)
    if p.is_alive():
        p.kill()
    if not result:
        # Reamark: ideally we would consider that all tests failed but we can't access number of tests here easily
        # so we use 21=the average number of tests for a smaple in the test split instead
        avg_number_tests = 21
        result = [[-1] * avg_number_tests]
    return result[0]


def compute_reward(prob_path, output_str, mode='train', public_test_cases=None, extra_info=False):
    """
    A utility function that computes the reward given problem path and output string of our model
    It is rewarded by the number of tests passed. When passing the same number of tests.
    """
    # from https://github.com/hendrycks/apps/blob/83d925041b1c43c32b56d444bb315f729f4ff633/eval/test_one_solution.py#L141
    try:
        which_tests_passed = check_correctness(prob_path, output_str, mode, public_test_cases)
        fixed = []
        for e in which_tests_passed:
            if isinstance(e, np.ndarray):
                e = e.item(0)
            if isinstance(e, np.bool_):
                e = bool(e)
            fixed.append(e)
        which_tests_passed = fixed
        # if not np.all(curr_res):
        #     print(f"Results were not all True: {curr_res}")
    except Exception as e:
        print(f"test framework exception = {repr(e)}{e}\n")
        which_tests_passed = []

    # How to read results [-2] = compile error, [-1] = runtime error [False] = failed test case [True] = passed test case")
    assert isinstance(which_tests_passed, list)
    pass_rate = np.mean(np.asarray(which_tests_passed) > 0) if len(which_tests_passed) > 0 else 0

    if COMPILE_ERROR in which_tests_passed or RUNTIME_ERROR in which_tests_passed:
        which_tests_passed = []
    if extra_info:
    #    info = {"compile_error": curr_res.count(-2) / len(curr_res), "runtime_error": curr_res.count(-1) / len(curr_res)}
    #    return pass_rate, info
        return pass_rate, which_tests_passed
    else:
        return pass_rate

def get_program_quality(s):
    """
    For now, only consider the length of the program. The shorter, the better.
    """
    return np.exp(- len(s) / 20)

