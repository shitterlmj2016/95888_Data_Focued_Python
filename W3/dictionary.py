# Creating Dictionaries with literals
word_frequency = {
    "Hello": 7,
    "hi": 10,
    "there": 45,
    "at": 23,
    "this": 77
}
print(word_frequency)

# Creating Dictionaries by passing parametrs in dict constructor
word_frequency = dict(Hello=7,
                      hi=10,
                      there=45,
                      at=23,
                      this=77)
print(word_frequency)

# Creating dictionaries with a List of tuples
list_of_tuples = [("Hello", 7), ("hi", 10), ("there", 45), ("at", 23), ("this", 77)]
word_frequency = dict(list_of_tuples)
print(word_frequency)

# Creating a Dictionary by a two lists
list_of_strings = ["Hello", "hi", "there", "at", "this"]
list_of_ints = [7, 10, 45, 23, 77, 99, 100, 101]
# Merge the two lists to create a dictionary
word_frequency = dict(zip(list_of_strings, list_of_ints))
print(word_frequency)

# or this way
a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
print(a['apple'])

a = {'one': 1, 'two': 'to', 'three': 3.0, 'four': [4, 4.0]}

# Update a dictionary
a['one'] = 1.0
print(a)

# Delete a single element
del a['one']
print(a)

# Delete all elements in the dictionary
a.clear()
print(a)

# Delete the dictionary
del a
# print(a) #error

######################################################################

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Put all keys of `dict1` in a list and returns the list
print(dict1.keys())
# Put all values saved in `dict1` in a list and returns the list
print(dict1.values())

# Double each value in the dictionary
double_dict1 = {}
for (k, v) in dict1.items():
    double_dict1[k] = v * 2
print(double_dict1)

# Double each value in the dictionary
double_dict1 = {k: v * 2 for (k, v) in dict1.items()}
print(double_dict1)

# make changes to the key values.
dict1_keys = {k * 3: v for (k, v) in dict1.items()}
print(dict1_keys)

numbers = range(10)
# Use dictionary comprehension
new_dict_comp = {n: n ** 2 for n in numbers if n % 2 == 0}

print(new_dict_comp)

# Initialize the `fahrenheit` dictionary
fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}

# Get the corresponding `celsius` values and create the new dictionary
celsius = {k: (float(5) / 9) * (v - 32) for (k, v) in fahrenheit.items()}

print(celsius)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Check for items greater than 2
dict1_cond = {k: v for (k, v) in dict1.items() if v > 2}

print(dict1_cond)

# Multiple If Conditions
dict1_doubleCond = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0}

print(dict1_doubleCond)

# triple
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

dict1_tripleCond = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0 if v % 3 == 0}

print(dict1_tripleCond)

# If-Else Conditions
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Identify odd and even entries
dict1_tripleCond = {k: ('even' if v % 2 == 0 else 'odd') for (k, v) in dict1.items()}

print(dict1_tripleCond)

# Nested Dictionary Comprehension
nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}
float_dict = {outer_k: {inner_k: float(inner_v) for (inner_k, inner_v) in outer_v.items()}
              for (outer_k, outer_v) in nested_dict.items()}

print(float_dict)



nested_dict = {'first':{'a':1}, 'second':{'b':2}}

for (outer_k, outer_v) in nested_dict.items():
    for (inner_k, inner_v) in outer_v.items():
        outer_v.update({inner_k: float(inner_v)})
nested_dict.update({outer_k:outer_v})

print(nested_dict)