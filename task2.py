# Q2. Write a decorator that measures the execution time of a function and logs the result to a file.

from functools import wraps
import time
import logging

logging.basicConfig(filename="log2.txt", level=logging.DEBUG)
logging.FileHandler('log2.txt', mode='w')


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        logging.info(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


class Calculator:
    @timeit
    def calculate_something(self, num):
        """
        an example function that returns sum of all numbers up to the square of num
        """
        total = sum((x for x in range(0, num**2)))
        return total

    def __repr__(self):
        return f'calc_object:{id(self)}'


if __name__ == '__main__':
    calc = Calculator()
    calc.calculate_something(10)
    calc.calculate_something(100)
    calc.calculate_something(1000)
    calc.calculate_something(2000)
    calc.calculate_something(5000)
