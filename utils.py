import time


def time_measure(func):
    start = time.time()
    return func(), (time.time() - start)


def print_answer(answer_text, func):
    result, elapsed_time = time_measure(func)
    print(f"{answer_text}: {result} (took {elapsed_time} seconds)")
