"""
For all questions replace pass with the appropriate code to satisfy the
requirements specified in the docstring. 

Topics:
- Importing packages
- List indexing
- Reading and writing files
-- Modes read, write, append, text, binary
-- File encodings
-- String vs binary reads
-- Reading by file, by line, by character
- Using the CSV reader package
-- Setting the delimiter
-- Reading CSV's as lists
-- Reading CSV's as dictionaries
-- Using the CSV writer package

Requirements:
1. you cannot use any material (source code, web searches, etc.) if you are found
to be using any material on the quiz you will fail the course.
"""
import csv


def quiz2_q1(file_name, bytes_to_read):
    """ 40 Points
    Opens the specified file in readonly binary mode and returns the 
    specified number of characters from the beginning of the file.
    
    Arguments:
        file_name {str} -- path to the file
    
    Returns:
        bytes object -- python bytes object representing the data read
    """
    with open(file_name, 'rb') as f:
        b = f.read(bytes_to_read)
        return b


def quiz2_q2(file_name, text):
    """ 40 Points
    Appends the text (as is without newlines or spaces) to the file
    
    Arguments:
        file_name {str} -- path to the file
        text {str} -- text to append to the file
    """
    with open(file_name, 'a', newline='')as f:
        f.write(text)


def quiz2_q3(file_name, encoding, delimiter, row_to_read):
    """7.5 Points
    Opens the CSV file with the specified encoding and delimiter. Returns the
    data row at the specified index as a list of values.

    Note: The header does not count as a data row
    
    Arguments:
        file_name {str} -- path to the file
        encoding {str} -- file encoding to use when opening the file e.g. utf-8
        delimiter {str} -- CSV file delimiter 
        row_to_read {int} -- Data row to return from the CSV
    
    Returns:
        list -- List of values from the CSV at the row specified.
    """
    with open(file_name, encoding=encoding) as f:
        reader = csv.reader(f, delimiter=delimiter)
        for (index, line) in enumerate(reader):
            if index == row_to_read:
                return line


def quiz2_q4(file_name, encoding, delimiter, row_to_read):
    """7.5 Points
    Opens the CSV file with the specified encoding and delimiter. Returns the
    data row at the specified index as an Ordered Dictionary.

    Note: The header does not count as a row
    
    Arguments:
        file_name {str} -- path to the file
        encoding {str} -- file encoding to use when opening the file e.g. utf-8
        delimiter {str} -- CSV file delimiter 
        row_to_read {int} -- Data row to return from the CSV
    
    Returns:
        OrderedDict -- Ordered Dictionary from the CSV at the row specified.
    """
    with open(file_name, encoding=encoding) as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        for (index, line) in enumerate(reader):
            if index + 1 == row_to_read:
                return line


def quiz2_q5(file_name, encoding, delimiter, row_to_read, column_to_read):
    """5 Points
    Opens the CSV file with the specified encoding and delimiter. Returns the
    value for the data row at the specified row and column index.

    Note: The header does not count as a row
    
    Arguments:
        file_name {str} -- path to the file
        encoding {str} -- file encoding to use when opening the file e.g. utf-8
        delimiter {str} -- CSV file delimiter 
        row_to_read {int} -- Data row to return from the CSV
    
    Returns:
        {str} -- The value at the specified data row and column index.
    """
    with open(file_name, encoding=encoding) as f:
        reader = csv.reader(f, delimiter=delimiter)
        for (index, line) in enumerate(reader):
            if index == row_to_read:
                return line[column_to_read]


# do not modify below this line

if __name__ == "__main__":
    quiz2_q1('quiz02/heinz-logo-16.3-final.jpg', 4)
    quiz2_q2('quiz02/heinz.txt', 'Welcome to the Heinz School')
    quiz2_q3('quiz02/people.txt', 'utf-8', '|', 3)
    quiz2_q4('quiz02/people.txt', 'utf-8', '|', 5)
    quiz2_q5('quiz02/movies.csv', 'utf-8', ',', 3, 2)
