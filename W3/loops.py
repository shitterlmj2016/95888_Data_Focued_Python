# for loops
for i in range(1, 10, 2):
    print(i)

# for...else loop
for i in range(1, 5):
    print(i)
    if i == 4:
        break
else:
    print('done')

# while...else loop
condition = True
i = 0
while condition:
    print(i)
    i += 1
    if i > 3:
        condition = False
else:
    print('done')

width = 5
chars = "*@"
for char in chars:
    for i in range(1, width): #从一加到width
        print(char * i)
    for j in range(width, 0, -1): #从width减到1
        print(char * j)


width = 5
chars = "*@"
for char in chars:
    for i in range(1, width):
        for spaces in range(width - i, 0, -1):
            print(' ', end='')
        print(char * i)
    for j in range(width, 0, -1):
        for spaces in range(width - j, 0, -1):
            print(' ', end='')
        print(char * j)