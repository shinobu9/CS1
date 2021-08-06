import functools
import time

@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fib_1(n, computed = {0: 1, 1: 1}):
     if n not in computed:
         computed[n] = fib_1(n-1, computed) + fib_1(n-2, computed)
     return computed[n]



n = int(input())


start_time = time.time()
#print(fib_1(n))
print(fib(n))

print("My program took", time.time() - start_time, "to run")