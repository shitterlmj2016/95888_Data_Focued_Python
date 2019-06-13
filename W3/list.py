# S = {x² : x in {0 ... 9}}
import timeit

S = []
for x in range(10):
    S.append(x ** 2)
print(S)

# S = {x² : x in {0 ... 9}}
S = [x ** 2 for x in range(10)]
print(S)

# V = (1, 2, 4, 8, ..., 2¹²)
V = []
for i in range(13):
    V.append(2 ** i)
print(V)

# V = (1, 2, 4, 8, ..., 2¹²)
V = [2 ** i for i in range(13)]
print(V)

# M = {x | x in S and x even}
M = [x for x in S if x % 2 == 0]
print(M)

numbers = range(0, 10)

# Create `new_list`
new_list = [n ** 2 for n in numbers if n % 2 == 0]

# Print `new_list`
print(new_list)

# time it
print(timeit.timeit('[n**2 for n in range(10) if n%2==0]', number=10000))

# Initialize the `kilometer` list
kilometer = [39.2, 36.5, 37.3, 37.8]

# Construct `feet` with `map()`
feet = map(lambda x: float(3280.8399) * x, kilometer)  # 注意用的是map

# Print `feet` as a list
print(type(feet), list(feet))

# Convert `kilometer` to `feet`
feet = [float(3280.8399) * x for x in kilometer]

# Print `feet`
print(feet)

# Filter `feet` to only include uneven distances
uneven = filter(lambda x: x % 2, feet)

# Check the type of `uneven`
type(uneven)

# Print `uneven` as a list
print(list(uneven))

# Construct `reduced_feet`
reduced_feet = sum([float(3280.8399) * x for x in kilometer])

# Print `reduced_feet`
print(reduced_feet)

# Define `uneven`
uneven = [int(x) for x in feet if x % 2]

# Print `uneven`
print(uneven)


#Multiple If Conditions
divided = [x for x in range(100) if x % 4 == 0 if x % 6 == 0]

print(divided)

#if...else Conditions

values = [x+1 if x >= 120000 else x+5 for x in feet]
print(values)


# Flatten `list_of_list`
list_of_list = [[1,2,3],[4,5,6],[7,8]]
flat = [y for x in list_of_list for y in x]
print(flat)

matrix = [[1,2,3], [4,5,6],[7,8,9]]

flat = [[row[i] for row in matrix] for i in range(len(matrix))]
print(flat)