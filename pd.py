"""
pandas
    loading from files
    apply
    setting data type as categorical
    boolean indexing
    dataframe slicing
    groupby and aggregation
"""

import numpy as np
import pandas as pd

s = pd.Series(["a", "b", "c", "a"], dtype="category")

data = np.array([['', 'Col1', 'Col2'],
                 ['Row1', 1, 2],
                 ['Row2', 3, 4]])

df = pd.DataFrame(data=data[1:, 1:],
                  index=data[1:, 0],  # 取第0列从第一行往后的
                  columns=data[0, 1:]
                  )  # 取第0行从第0列往后

print(df)

# Take a 2D array as input to your DataFrame
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(my_2darray)

# Take a dictionary as input to your DataFrame
my_dict = {
    1: ['1', '3'],
    2: ['1', '2'],
    3: ['2', '4']}

print(my_dict)

# Take a DataFrame as input to your DataFrame
my_df = pd.DataFrame(data=[4, 5, 6, 7], index=range(0, 4), columns=['A'])
print(my_df)

# Take a Series as input to your DataFrame
my_series = pd.Series({
    "Belgium": "Brussels",
    "India": "New Delhi",
    "United Kingdom": "London",
    "United States": "Washington"})

print(my_series)

'''
Note that the index of your Series (and DataFrame) contains the keys of the original dictionary, but that they are sorted: Belgium will be the index at 0, while United States will be the index at 3.
'''

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))

# Use the `shape` property
print(df)

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))

# Use the `shape` property
print(df.shape)

# Or use the `len()` function with the `index` property
print(len(df.index))

print(list(df.columns.values))
print(list(df.index.values))


def create_df():
    vals = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    dict = {k: v for (k, v) in zip('ABC', vals)}
    df = pd.DataFrame(dict)
    return df


df = create_df()
print(df)

# Using `iloc[]`
print(df.iloc[0][0])  # 通过index取数据

# Using `loc[]`
print(df.loc[0]['A'])  # 通过label取数据

# Using `at[]`
print(df.at[0, 'A'])

# Using `iat[]`
print(df.iat[0, 0])

# Use `iloc[]` to select row `0`
print(df.iloc[0])

# Use `loc[]` to select column `'A'`
print(df.loc[:, 'A'])

# Print out your DataFrame `df` to check it out
print(df)

# Set 'C' as the index of your DataFrame
print(df.set_index('C'))

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  index=[2, 'A', 4],
                  columns=[48, 49, 50])
print(df)
# Pass `2` to `loc`
print(df.loc[2])

# Pass `2` to `iloc`
print(df.iloc[2])

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  index=[2.5, 12.6, 4.8],
                  columns=[48, 49, 50])
print(df)

# This will make an index labeled `2` and add the new values
df.loc[2] = [11, 12, 13]
print(df)

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=['A', 'B', 'C'])

# Use `.index`
df['D'] = df.index

# Print `df`
print(df)

# Append a column to `df`
df.loc[:, 4] = pd.Series(['5', '6', '7'], index=df.index)

# Print out `df` again to see the changes
print(df)

# Use `reset_index()` to reset the values.
x = df.reset_index(level=0, drop=True)
print(x)

# Deleting an Index from Your DataFrame


df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]),
                  index=[2.5, 12.6, 4.8, 4.8, 2.5],
                  columns=[48, 49, 50])

print(df)

x = df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index')
print(x)

# Check out the DataFrame `df`
df = create_df()
print(df)

# Drop the column with label 'A'
df.drop('A', axis=1, inplace=True)
print(df)

# Drop the column with label 'A'
df.drop(0, axis=0, inplace=True)  # 0 是 row, 1 是 col
print(df)

# Check out your DataFrame `df`
df = create_df()
df = df.append({'A': 1, 'B': 2, 'C': 3}, ignore_index=True)
print(df)

reviews = pd.read_csv("ign.csv")
print(reviews.head(3))
print(reviews.shape)
print(reviews.iloc[0:5, :])  # exclusive

reviews = reviews.iloc[:, 1:]
print(reviews.head())

print(reviews.shape)

print(reviews.loc[0:5, :])
print(list(reviews.index)[:20])

some_reviews = reviews.iloc[10:20, ]
print(some_reviews.head())

print(reviews.loc[:5, "score"])

print(
    reviews.loc[:5, ["score", "release_year"]])

print(reviews.loc[[0, 3], ["score", "release_year"]])

print(type(reviews["score"]))

s1 = pd.Series([1, 2])
print(s1)

s2 = pd.Series(["Boris Yeltsin", "Mikhail Gorbachev"])
print(s2)

# specify the index labels
frame = pd.DataFrame(
    [
        [1, 2],
        ["Boris Yeltsin", "Mikhail Gorbachev"]
    ],
    index=["rank", "name"],
    columns=["person1", "person2"]
)
print(frame)

print(reviews["title"].head())

###############################################################
# boolean
score_filter = reviews["score"] > 9
print(score_filter)
print(reviews[score_filter])

# setup the boolean filtr
xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")

# select the data based on the filter
filtered_reviews = reviews[xbox_one_filter]

# display the first 5 results
print(filtered_reviews.head())

data = pd.read_csv("thanksgiving-2015-poll-data.csv", encoding="Latin-1")
print(data.head())

# investigate respondent values
print(data["Do you celebrate Thanksgiving?"].unique())

# get respondent counts per response
print(data["What is your gender?"].value_counts(dropna=False))

print(data["What type of cranberry saucedo you typically have?"].value_counts())

column_name = "What type of cranberry saucedo you typically have?"
homemade_mask = data[column_name] == "Homemade"
print(homemade_mask.head())

homemade = data[homemade_mask]
print(homemade)

canned = data[data[column_name] == "Canned"]

##########################group########################
column_name = "What type of cranberry saucedo you typically have?"
grouped = data.groupby(column_name)
print(grouped)

print(grouped.groups)

print(grouped.size())

# for name, group in grouped:
#     print(name)
#     print('\t', group.shape)
#     print('\t', type(group))
#
# print(grouped["income"].size())

# Aggregating values in groups
# print(grouped["income"].agg(np.mean))


grouped = data.groupby(
    ["What type of cranberry saucedo you typically have?",
     "What is typically the main dish at your Thanksgiving dinner?"])
print(grouped.agg(np.mean))

# grouped["income"].agg([np.mean, np.sum, np.std]).head(10)


grouped = data.groupby("How would you describe where you live?")[
    "What is typically the main dish at your Thanksgiving dinner?"]
print(grouped)
print(grouped.apply(lambda x: x.value_counts()))

# aggreating
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
print(ser)

df = pd.DataFrame({'A': rng.rand(5),
                   'B': rng.rand(5)})
print(df)

"""
Aggregation	Description
count()	Total number of items
first(), last()	First and last item
mean(), median()	Mean and median
min(), max()	Minimum and maximum
std(), var()	Standard deviation and variance
mad()	Mean absolute deviation
prod()	Product of all items
sum()	Sum of all items
"""

# Group
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key', 'data'])
print(df)

print(df.groupby('key').sum())
