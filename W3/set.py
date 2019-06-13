x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
print(x)

y = set(('foo', 'bar', 'baz', 'foo', 'qux'))
print(y)

s = 'data focused python'
words = s.split(' ')
print(set(words))

x = {'foo', 'bar', 'bar', 'foo', 'qux'}
print(type(x), x)

y = set('foo')
# y.add('apple')
print(type(y), y)

y = set()
print(type(y))

x = {'foo', 'bar', 'baz'}
print(len(x))
print('bar' in x)

#Operators vs. Methods
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
union_x = x1 | x2
print(union_x)


a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

print(a.union(b, c, d))
print(a | b | c | d)



x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1.intersection(x2))
print(x1 & x2)


a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

print(a.intersection(b, c, d))
print(a & b & c & d)



a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}

print(a.difference(b, c))
print(a - b - c)

#抑或
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1.symmetric_difference(x2))
print(x1 ^ x2)


# Disjoint
# Determines whether or not two sets have any elements in common.

# x1.isdisjoint(x2) returns True if x1 and x2 have no elements in common:
x1 = {1, 3, 5}
x2 = {2, 4, 6}

print(x1.isdisjoint(x2))

#Is Subset
#Determine whether one set is a subset of the other.

# In set theory, a set x1 is considered a subset of another set x2 if every element of x1 is in x2.

# x1.issubset(x2) and x1 <= x2 return True if x1 is a subset of x2:

x1 = {'foo', 'bar', 'baz'}
print(x1.issubset({'foo', 'bar', 'baz', 'qux', 'quux'}))


x1 = {'foo', 'bar', 'baz'}
print(x1.issuperset({'foo', 'bar'}))


#Frozen Sets immutable
x = frozenset(['foo', 'bar', 'baz'])
print(x)


# Set Comprehension
import random
from random import randint
seed = 1234
random.seed(seed)
x = 0
y = 5
a = [randint(x, y) for i in range(0, 10)]
print(a)


random.seed(seed)
x = 0
y = 5
b = {randint(x, y) for i in range(0, 10)}
print(b)


random.seed(seed)
a = ['Even' if i % 2 else 'Odd' for i in range(10)]
print(a)

random.seed(seed)
b = {'Even' if i % 2 else 'Odd' for i in range(10)}
print(b)