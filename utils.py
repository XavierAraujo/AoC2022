import time


def time_measure(func):
    start = time.time()
    return func(), (time.time() - start)


def print_answer(answer_text, func):
    result, elapsed_time = time_measure(func)
    print(f"{answer_text}: {result} (took {elapsed_time} seconds)")


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def flatten_list(l):
    return [item for sublist in l for item in sublist]