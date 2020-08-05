import time
import random
import math


start = time.time()


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


c = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if (x, y) not in c:
        c[x, y] = slowfun_too_slow(x, y)
    return c[x, y]


##########################################################################
# Do not modify below this line!


for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')  # Total Time: 3.19 seconds
    # print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}') # Total Time: 3679.38 seconds (1 hr 1 min)


end = time.time()

print('-'*75)
total = end-start
print(f'Total Time: {total:.2f} seconds')
