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
list_of_tuples = [("Hello" , 7), ("hi" , 10), ("there" , 45),("at" , 23),("this" , 77)]
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


a = {'one': 1, 'two': 'to', 'three': 3.0, 'four': [4,4.0]}

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
print(a) #error