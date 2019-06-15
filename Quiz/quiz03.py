import random
import csv

"""
For all questions replace pass with the appropriate code to satisfy the
requirements specified in the docstring. 

Topics:
1 on set comprehension
2 on list comprehensions
2 on dictionary comprehensions

You can expect to see:
1. use of conditionals (e.g. if statements) for both filtering and value generation
2. nested comprehensions

Requirements:
1. you cannot use any material (source code, web searches, etc.) if you are found
to be using any material on the quiz you will fail the course.
"""


def quiz3_q1():
    """40 Points
    Use a list comprehension to create a list of 1000 random integers with a
    seed of 12345 between 1000 and 2000 (inclusive). Return the list
    
    Hints:
    random.randint(a, b) generates a random integer between a and b (inclusive) 
    
    random.seed(seed) sets the pseudo-random generator a seed so you can 
    create reproducible random sequences
    
    range(a) creates an iterable sequence of numbers between 0 to a (exclusive)
    
    Returns:
        list -- list of random integers
    """
    seed = 12345
    random.seed(seed)
    list = [random.randint(1000, 2000) for i in range(0, 1000)]
    return list


def quiz3_q2(data, x, y, z):
    """40 Points   
    Use a list comprehension to create a list of values from data that are 
    greater than or equal to x but less than y and evenly divisible by z

    Arguments:
        data {list} -- list of numbers
        x {int} -- low end of the value range (inclusive)
        y {int} -- high end of the value range (exclusive)
        z {int} -- divisor e.g. 
            dividend = 6, divisor (z) = 3
            dividend is evenly divisible by z

            dividend = 5, divisor (z) = 3
            dividend is not evenly divisible by z
    Returns:
        list -- list of numbers
    """
    list = [i for i in range(x, y) if i % z == 0]
    return list


def quiz3_q3(values):
    """7.5 Points
    Use a list comprehension to flatten the list of lists
    
    Arguments:
        values {list} -- list of lists
    
    Returns:
        list -- the flattened list
    """
    list = [y for x in values for y in x]
    return list


def quiz3_q4(keys, values):
    """7.5 Points
    Use a list comprehension to create a dictionary with keys from the keys
    list and values from the values list.
    
    Arguments:
        keys {list} -- list containing the keys for the dictionary
        values {list} -- list containing the values for the dictionary

    Hints:
    zip(a, b) will iterate over list a and list b and return a tuple that
    contains elements from list a and list b at the same index position
    
    Returns:
        dictionary -- dictionary of key value pairs
    """
    dic = dict(zip(keys, values))
    return dic


def quiz3_q5(text, exclude):
    """5 Points
    Use a set comprehension to create a set of distinct words contained in the 
    text. The set should not include any of the words in the exclude list.
    
    Arguments:
        text {str} -- string to process
        exclude {list} -- list of strings to exclude from the set

    Hints:
    str.lower() converts a string to lower case
    
    list.split(delimiter) splits a string into a list of strings based on the
    delimiter

    list membership can be tested with the 'in' keyword e.g. 1 in [1, 2, 3]
    list exclusion can be tested using 'not in'

    Returns:
        set -- set containing strings

    Expected Value:
    
    {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'}
    """
    my_set = {x for x in (set(text.split(' ')) - set(exclude))}
    return my_set

# do not modify below this line

if __name__ == "__main__":
    ans_q1 = quiz3_q1()
    print('Question 1', ans_q1[:10], '\n')

    ans_q2 = quiz3_q2(ans_q1, 1800, 1900, 3)
    print('Question 2', ans_q2, '\n')

    ans_q3 = quiz3_q3(list([list('abcd'), list('efgh'), list('ijkl')]))
    print('Question 3', ans_q3, '\n')

    ans_q4 = quiz3_q4(list(range(1, 11)), list('abcdefghijklmnopqrstuvwxyz'))
    print('Question 4', ans_q4, '\n')

    text = "Technology is impacting everything we do from the way we live our lives to the way we do business from the way we connect with others to the way we monitor our own health from the way we analyze our surroundings to the way we navigate our world Policy defines priorities and guides action The creation deployment and re-visioning of smart policies through rigorous inquiry and evidence-based decision-making has always been a key component of human innovation and progress Policy and technology have historically been separate domains but more and more the lines between the two—and the demands they place on each other—are blurring And of critical interest is how this impacts People The next generation of leaders must deeply understand this critical point of intersection: People policy and technology The connections between the three define our time and will continue to shape the future of humankind At Heinz College we’ve understood this since our founding Our first Dean William Cooper had a vision of educating men and women for intelligent action” and this is still our primary objective In our educational programs we accomplish this through a foundation of data analytics technology and experiential learning Regardless of whether you come here to study Arts Management or Information Security or anything in between your experience will be built on these elements Our research programs are best described as data-intensive social science Our economists statisticians operations researchers computer scientists and management experts sit side by side collaborating constantly and not sitting in traditional departmental silos For this reason they are able to approach complex societal problems in an altogether different way The unique co-location of our two schools the School of Public Policy and Management and the School of Information Systems and Management offers opportunities for collaboration that simply cannot be duplicated elsewhere We also offer two groundbreaking Joint Degree Programs with the CMU College of Fine Arts Our faculty and students know that exciting things happen when disciplines collide when differing perspectives come into contact with one another I encourage you to thoroughly explore this website not only to learn more about our programs but to find stories about the impact that members of the Heinz community have had on the world through groundbreaking research and projects professional accomplishments and entrepreneurial ventures We hope that someday you will join their ranks"
    ans_q5 = quiz3_q5(text, exclude=['and', 'the', 'a'])
    print('Question 5', ans_q5, '\n')
