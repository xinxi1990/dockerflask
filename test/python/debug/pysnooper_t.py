

import pysnooper
import random
@pysnooper.snoop()
def foo():
    lst = []
    for i in range(10):
        lst.append(random.randrange(1, 1000))
    lower = min(lst)
    upper = max(lst)
    mid = (lower + upper) / 2
    print(lower, mid, upper)
foo()