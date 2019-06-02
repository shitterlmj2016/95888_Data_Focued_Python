"""
For all questions replace pass with the appropriate code to satisfy the
requirements specified in the docstring. The expected output is shown below.

Note: The question heading e.g. Question 1 is printed for you as is the newline
between questions. Every other print statement is expected to be in the 
following format:

<line_number>:<space><your output>

for instance:

Question 1
1: My favorite color is red.

Question 2
1: My favorite color is blue!
2: My favorite color is blue!
3: My favorite color is blue!

Requirements:
1. output must be exact, no extra spaces or newlines
2. you cannot use any material (source code, web searches, etc.) if you are found
to be using any material on the quiz you will fail the course.
"""


def quiz1_q1(color, punctuation):
    """ 50 Points
    Prints your favorite color with a specific punctuation mark.

    Arguments:
        color {String} -- color
        punctuation {String} -- punctuation mark
    """
    print(f"1: My favourite color is {color}{punctuation}")



def quiz1_q2(color, punctuation, loops):
    """ 30 Points
    Prints your favorite color with a specific punctuation N times.
    
    Arguments:
        color {String} -- color
        punctuation {String} -- punctuation mark
        loops {int} -- number of times to print
    """
    for i in range(1, loops + 1):
        print(f"{i}: My favourite color is {color}{punctuation}")



def quiz1_q3(colors):
    """ 7.5 Points
    Prints your favorite colors once per color.

    Example output:
    1: My favorite color is red.
    2: My favorite color is blue.
    3: My favorite color is green.
    
    Arguments:
        colors {list} -- list of colors represented as a String
    """
    for index, value in enumerate(colors):
        print(f"{index + 1}: My favourite color is {value}.")



def quiz1_q4(color, punctuations):
    """ 7.5 Points
    Prints your favorite color N times, once per punctuation in the 
    punctuation list.

    Example output:
    1: My favorite color is blue.
    2: My favorite color is blue!
    3: My favorite color is blue?
    
    Arguments:
        color {String} -- color
        punctuations {list} -- list of punctuation marks as a String
    """
    for index, value in enumerate(punctuations):
        print(f"{index + 1}: My favourite color is {color}{value}")



def quiz1_q5(colors, punctuations):
    """ 5 Points
    Prints each of your favorite colors once with the corresponding 
    punctuation. Each punctuation mark correspondes to the color at the same 
    list position. 
    
    Example output:
    1: My favorite color is red.
    2: My favorite color is blue!
    3: My favorite color is green?
    
    Arguments:
        colors {list} -- list of colors represented as a String
        punctuations {list} -- list of punctuation marks as a String
    """
    for index, value in enumerate(punctuations):
        print(f"{index + 1}: My favourite color is {colors[index]}{value}")



# do not modify anything below this line
if __name__ == "__main__":
    print("\nQuestion 1")
    quiz1_q1("red", ".")

    print("\nQuestion 2")
    quiz1_q2("blue", "!", 3)

    print("\nQuestion 3")
    quiz1_q3(["red", "blue", "green"])

    print("\nQuestion 4")
    quiz1_q4("blue", [".", "!", "?"])

    print("\nQuestion 5")
    quiz1_q5(["red", "blue", "green"], [".", "!", "?"])
