import time
import functools
from line_profiler import LineProfiler
from memory_profiler import profile


def memory_and_recursion_usage(func):
    @functools.wraps(func)
    @profile
    def wrapper(*args, **kwargs):
        memory_before = memory_usage_psutil()

        result = func(*args, **kwargs)
        memory_after = memory_usage_psutil()

        print(f"{func.__name__} использовала {memory_after - memory_before} MB памяти")

        return result

    return wrapper


def memory_usage_psutil():
    import psutil
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss / 1024 / 1024


def count_operations(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler = LineProfiler()
        wrapped = profiler(func)
        result = wrapped(*args, **kwargs)
        profiler.print_stats()
        return result

    return wrapper


def performance_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} выполнилась за {execution_time:.6f} секунд")
        return result

    return wrapper
