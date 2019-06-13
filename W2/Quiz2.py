"""
1. from .. import // import
    from modname import *



 Mode	Description
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)






2. f = open('file.txt')
f = open("test.txt", 'w')  # write in text mode
f = open("python.png",'r+b') # read and write in binary mode
f = open("file.txt", mode='r', encoding='utf-8')
f = open("file.txt", encoding='utf-8')
# perform file operations
f.close()

try:
   f = open("file.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()

with open("file.txt", 'w', encoding='utf-8') as f:
   f.write("hello class\n" )
   f.write("python is fun\n\n")
   f.write("let's get started\n")

f.tell() # get the current file position
f.seek(0) # bring file cursor to initial position
f.read() # read the entire file

for line in f:
    print(line, end='')

f.readline()

"""

f = open("C:\\Users\\91593\\Desktop/1.txt")
s = f.read(5) #读取限定长度的字符
print(s)
# for line in f :
#     #print(line, end = '') #去掉空行
#


#csv
# open and print line by line
# with open('mock.csv') as f:
#     for line in f:
#         print(line)
#
# with open('mock.csv') as f:
#     # use enumerate to get the index as you iterate
#     for index, line in enumerate(f):
#         print(index, line)
#
# with open('mock.csv') as f:
#     for index, line in enumerate(f):
#         # handle the header differently
#         if index == 0:
#             print("header", index, line)
#         else:
#             print("row", index, line)


import csv
with open('mock.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)

with open('mock.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for index, row in enumerate(reader):
        if index == 0:
            print(f'{", ".join(row)}')
        else:
            print(f'id: {row[0]} first_name: {row[1]} last_name: {row[2]} email: {row[3]}')


# Reading CSV Files Into a Dictionary With csv
with open('mock.csv') as f:
    reader = csv.DictReader(f)
    for index, row in enumerate(reader):
        if index == 0:
            print(f'{", ".join(row)}')
        else:
            print(f'id: {row["id"]} first_name: {row["first_name"]} last_name: {row["last_name"]} email: {row["email"]}')

# csv write
with open('scores.csv', mode='w') as employee_file:
    writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['2019-05-01', 'Pirates', 0, 'Cubs', 10])
    writer.writerow(['2019-05-15', 'Reds', 7, 'Pirates', 0])

# csv write dictionary
with open('scores.csv', mode='w') as csv_file:
    fieldnames = ['date', 'home_team', 'home_score', 'away_team', 'away_score']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'date': '2019-05-01', 'home_team': 'Pirates', 'home_score': 0, 'away_team': 'Cubs', 'away_score': 10})
    writer.writerow({'date': '2019-05-15', 'home_team': 'Reds', 'home_score': 7, 'away_team': 'Pirates', 'away_score': 0})