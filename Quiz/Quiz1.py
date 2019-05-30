print("hello word")
name = "Eric"
age = 74
# f formatting

print(f"Hello, {name}. You are {age}.")

profession = "doctor"
affiliation = "comedian"

message = (f"Hi {name}. "
           f"You are a {profession}. "
           f"You were in {affiliation}.")

print(message)

print("haha" + str(1) + 'hoho')

# loop
for i in range(0, 10):
    print(i)

# indexing
lst = ["aa", 2, 3, "tony", "sujata", "gary"]
print(lst[0])

# enumerate
for index, value in enumerate(lst, 2):
    print(f"{index}: {value}")
