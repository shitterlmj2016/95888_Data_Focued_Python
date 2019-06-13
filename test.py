import math

a = {1: 'a', 2: 'b', 3: 'c'}
print({k + 1: v for (k, v) in a.items() if k > 1 if k < 3})
