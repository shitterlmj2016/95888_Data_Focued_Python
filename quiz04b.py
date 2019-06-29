import numpy as np
import pandas as pd


def quiz4_q1():
    """15 Points
    Create a 2-dimensional 6x4 Numpy array using arange that contains
    values between 0 and 23 (inclusive). Slice out the values in 
    the 3rd and 4th rows and the 3rd column.

    ex:
    1st  2nd 3rd 4th
    [[0  1    2   3] # 1st row
    [ 4  5    6   7]
    [ 8  9   10  11]
    [12 13   14  15]
    [16 17   18  19]
    [20 21   22  23]] 

    ans:
    [[10]
    [14]] 
   
    Returns:
        numpy.ndarray -- Numpy array containing the result
    """
    array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]])
    return np.resize(array[[2, 3], 2], (2, 1))


def quiz4_q2():
    """15 Points
    Create a 3-dimensional Numpy array that represents 100 years worth of data.
    Each year is broken down into 3-month quarters. The array should contain
    0's at every position. Then set the value for the 2nd month of 
    the 2nd and 3rd quarter for every year to 9.

    ex:
    # year 1
    [[[0. 0. 0.] # quarter 1
    [0. 0. 0.]   # quarter 2
    [0. 0. 0.]   # quarter 3
    [0. 0. 0.]]  # quarter 4

    # year2
    [[0. 0. 0.]
    [0. 0. 0.]
    [0. 0. 0.]
    [0. 0. 0.]]] 

    ans:
    [[[0. 0. 0.]
    [0. 9. 0.]
    [0. 9. 0.]
    [0. 0. 0.]]

    [[0. 0. 0.]
    [0. 9. 0.]
    [0. 9. 0.]
    [0. 0. 0.]]] 
    
    Returns:
        numpy.ndarray -- Numpy array containing the result
    """
    array = np.zeros((100, 4, 3), dtype=np.int32)
    array[..., [1, 2], [1]] = 9
    return array
    pass


def quiz4_q3():
    """7.5 Points
    Create a numpy array of 10,000 values between 0 and 9,999. Return a
    numpy array that contains the values that are between 5,000 and 6,000
    which are evenly divisible by 7.
    
    Returns:
        numpy.ndarray -- Numpy array containing the result
    """
    array = np.array([i for i in range(0, 10000)])
    mask = (array >= 5000) & (array <= 6000) & (array % 7 == 0)
    sub_array = array[mask]
    return sub_array


def quiz4_q4():
    """7.5 Points
    Create a 3-dimensional 10x10x10 numpy array containing values between
    0 and 999. Write a lambda that cubes a value. Use the lambda to return
    a numpy array of the cubed values.
    
    Returns:
        numpy.ndarray -- Numpy array containing the result
    """

    array = np.arange(0, 1000, 1)

    array = np.resize(array, (10, 10, 10))

    return array
    # new_array = np.fromfunction(lambda i: i * i * i, (0, 1000), dtype=int)
    # print(new_array)
    # # array = [a: lambda x: x * x * x]
    pass


def quiz4_q5():
    """5 points
    1. Create a numpy array that contains characters a through z, call this x
    2. Create a lambda that converts a character to its ascii value
    3. Create a numpy array that contains x minus 32 minus for value of x, call this y
    4. Create a lambda that converts an ascii value to its character representatioon
    5. Create a numpy array that contains the converted characters, call this z
    6. Return x, y, and z

    x = ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z'] 
    y = [65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90] 
    z = ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z']

    Hints:
    1. np.vectorize will takes a function and returns a vectorized version of
    the passed in function.
    2. ord('a') returns 97
    3. chr(97) returns 'a'
    
    Returns:
        tuple -- tuple containing x, y, and z which are numpy arrays
    """
    x = np.array(
        ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z'])

    # print(y)
    return x


def quiz4_q6(file_name):
    """15 Points
    Load the the file into a pandas DataFrame and return the DataFrame

    Arguments:
        file_name {str} -- path to a csv file to load

    Returns:
        pandas.DataFrame -- pandas DataFrame
    """
    data = pd.read_csv(file_name, encoding="UTF-8")
    return data
    pass


def quiz4_q7(data):
    """15 Points
    Create a new column named gender_code where 1 represents men and
    0 represents women. Leave all unspecified values unchanged. Set the
    datatype of the new column to category.

    Arguments:
        data {pandas.DataFrame} -- pandas Dataframe

    Ex:
         first_name      last_name     ...     movie_rating gender_code
    0        Monroe         Scarff     ...             52.0           1
    1        Sayers       Koenraad     ...             74.0           1
    2      Staffard         Clague     ...             66.0           1
    ...
    997      Giusto       Wildbore     ...             70.0           1
    998        Rufe          Prout     ...              NaN           1
    999     Neville       Gatfield     ...             61.0           1

    Returns:
        pandas.DataFrame -- pandas DataFrame
    """
    gender = data["gender"]
    gender = gender.tolist()
    code = []

    print(gender[1])
    print(gender[1] == "male")

    for i in gender:
        if i == "Male" or i == "M" or i == "m" or i == "male":
            code.append(1)

            if i == "Female" or i == "female" or i == "f" or i == "F":
                code.append(0)
            else:
                code.append("")

    code = pd.Series(code)
    print(code)
    data["gender_code"] = code
    return data


def quiz4_q8(data):
    """7.5 Points
    Return a pandas DataFrame that only contains the genre and rating
    columns and maintains the index.

    Arguments:
        data {pandas.DataFrame} -- pandas Dataframe

    Ex:
                movie_genre  movie_rating
    0                Comedy          52.0
    1                 Drama          74.0
    2                  IMAX          66.0
    3                 Crime           NaN
    ...
    997               Drama          70.0
    998         Documentary           NaN
    999               Drama          61.0


    Returns:
        pandas.DataFrame -- pandas DataFrame
    """
    return data.loc[:, ["movie_genre", "movie_rating"]]


def quiz4_q9(data):
    """7.5 Points
    Return a pandas DataFrame for movies with a rating greater than 75 that
    only contains the genre, title, and rating columns and maintains the index.

    Arguments:
        data {pandas.DataFrame} -- pandas Dataframe

    Ex:
         movie_genre                                        movie_title  movie_rating
    6          Drama                                     Longshots, The          82.0
    34         Drama                                    The Killing Jar          76.0
    42   Documentary                                    Steal This Film          79.0
    ...
    968      Mystery                                     Eyes Wide Shut          83.0
    989  Documentary                               DysFunktional Family          83.0

    Returns:
        pandas.DataFrame -- pandas DataFrame
    """
    sub_data = data.loc[:, ["movie_genre", "movie_titie", "movie_rating"]]
    mask = sub_data["movie_rating"] > 75
    return sub_data[mask]
    pass


def quiz4_q10(data):
    """5 Points
    Return a pandas DataFrame that contains the average, standard deviation,
    min, median, and max values for the movie ratings by movie genre.

    Arguments:
        data {pandas.DataFrame} -- pandas Dataframe

    Ex:
                        movie_rating
                               mean        std   min median   max
    movie_genre
    (no genres listed)    64.142857   6.962485  53.0   64.0  73.0
    Action                65.540000   8.179641  48.0   66.5  82.0
    Adventure             65.160000   9.771046  50.0   63.0  82.0
    ...
    Thriller              65.000000  10.132456  37.0   65.0  91.0
    War                   64.950000   5.977810  55.0   65.5  76.0
    Western               68.583333   5.195423  55.0   69.0  75.0

    Returns:
        pandas.DataFrame -- pandas DataFrame
    """
    col0 = data.groupby("movie_rating").mean()
    # col1 = data.groupby("movie_rating").sum()
    col2 = data.groupby("movie_rating").std()
    col3 = data.groupby("movie_rating").min()
    col4 = data.groupby("movie_rating").median()
    col5 = data.groupby("movie_rating").max()

    re = data.groupby("movie_rating")
    re["mean"] = col0
    re["std"] = col2
    re["min"] = col3
    re["median"] = col4
    re["max"] = col5
    return re


# do not modify below this line

if __name__ == "__main__":
    ans_q1 = quiz4_q1()
    print('Question 1\n', ans_q1, '\n')

    ans_q2 = quiz4_q2()
    print('Question 2\n', ans_q2, '\n')

    ans_q3 = quiz4_q3()
    print('Question 3\n', ans_q3, '\n')

    ans_q4 = quiz4_q4()
    print('Question 4\n', ans_q4, '\n')

    ans_q5 = quiz4_q5()
    # print('Question 5\n',
    #       'x =', ans_q5[0], '\n',
    #       'y =', ans_q5[1], '\n',
    #       'z =', ans_q5[2], '\n')
    #
    ans_q6 = quiz4_q6('quiz04b.csv')
    # print('Question 6\n', ans_q6, '\n')
    #
    ans_q7 = quiz4_q7(ans_q6)
    # print('Question 7\n', ans_q7, '\n')
    #
    ans_q8 = quiz4_q8(ans_q7)
    # print('Question 8\n', ans_q8, '\n')
    #
    ans_q9 = quiz4_q9(ans_q7)
    # print('Question 9\n', ans_q9, '\n')
    #
    ans_q10 = quiz4_q10(ans_q7)
    # print('Question 10\n', ans_q10, '\n')
