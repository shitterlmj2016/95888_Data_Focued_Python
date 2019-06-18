import math
from pprint import pprint

a = {'a': 12, 'b': 11, 'c': 10}
a = sorted(a, key=lambda k: a[k])
pprint(a)
