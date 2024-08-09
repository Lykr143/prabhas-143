# wap to reverse a list without slicing or reverse function
import programs
l = [4, 5, 7, 9, 6]
l1 = []  # empty list to store the output#[5, 4,]
for i in l:  # iterate through each element
    l1.insert(0, i)
print(l1)

# wap to print the unique elements of a list
# l = [2, 3, 2, 1, 4, 3, 7, 5]


def unique_elements(l):
    op = []
    for i in l:
        if l.count(i) == 1:
            op.append(i)
    return op


print(unique_elements([2, 3, 2, 1, 4, 3, 7, 5]))

# wap to print the duplicate elements of a list

# wap to print the unique elements of a list


def duplicate_elements(l):
    result = []
    for i in l:
        if l.count(i) > 1 and i not in result:
            result.append(i)
    return result


print(duplicate_elements([2, 3, 2, 1, 4, 3, 7, 5]))


# wap to check if the number is a prime or noti
def is_prime(num):
    if num > 1:
        for i in range(2, num):  # it will check the factors 2, 23
            if num % i == 0:
                print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


is_prime(23)
is_prime(3)
is_prime(1)
is_prime(-2)


# wap to print the common elements from the list
# (do not print the same element multiple elements)

l1 = [1, 2, 3, 4]
l2 = [2, 4, 6, 2, 7]
op = []
for i in l1:
    if i in l2:
        op.append(i)
print(op)

print([i for i in l1 if i in l2])


# wap to print the vowels from given string
def print_vowels(string):
    op = []
    for i in string:
        if i in "aeiou":
            op.append(i)
    return op


print(print_vowels("hello world"))

"""
wap to print a dictionary which contains the first character
of every word in below string as keys and list of words which starts with
specific character as values
"""
string = "python is my favorite programming language im"
d = {}
for word in string.split():
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]].append(word)
print(d)

# capitalize the first character of all sentences in a paragraph
s = "how are you? i am fine. where do you live?"
res = ''
flag = False
for j, i in enumerate(s):
    if not i.isalnum() and i != " ":
        flag = True
        res = res + i
    elif i == " ":
        res = res + i
    elif flag == True or j == 0:
        flag = False
        res = res + i.upper()
    else:
        res = res + i
print(res)


data = """yeswanth bangalore IBM 15000
bharath bangalore wipro 20000
prabhas hyderbad TCS 25000"""


# wap to print average salaries of employees who are working in bangalore
op = []
location = "bangalore"
lines = data.splitlines()
for line in lines:
    row = line.split()
    if location in row:
        op.append(int(row[-1]))
print(sum(op)/len(op))


def average_salaries(data, location):
    result = [int(row.split()[-1])
              for row in data.splitlines() if location in row]
    print(sum(result) / len(result))


average_salaries(data, "bangalore")

# wap to print display list of employees names working in bangalore


def emp_names(data, location):
    res = [row.split()[0] for row in data.splitlines() if location in row]
    print(res)


emp_names(data, "bangalore")

# wap to print company names located in bangalore


def company_names(data, location):
    result = [row.split()[2] for row in data.splitlines() if location in row]
    print(result)


company_names(data, "bangalore")
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# wap to print the flatten list
"""
flatten takes a nested list and returns a new list with all the elements
of the nested list flattened into a single list
initialize the fla_list to accept the flattened elements
loop over each nested list in the input_list
loop over each individual element inside the nested list and append it to flat_list"""


def flatten(l):
    flat_list = []
    for nested_list in l:
        for sub_list in nested_list:
            flat_list.append(sub_list)
    return flat_list


print(flatten(l))

outpt = [j for i in l for j in i]
print(outpt)

info = """Name Location Email
Asma Hyderbad asma.123@gmail.com
dinesh Bangalore dinesh.143@gmail.com
hari Bangalore 1_sarma@gmail.com"""

rows = info.splitlines()[1:]
d = {}
for i in rows:
    name, location, username = i.split()
    #print(name, location, username)
    username = username.split("@")[0]
    # print(username)
    username = username.replace(".", "_")
    d[name] = {"location": location, "username": username}
print(d)
# print(d["hari"])
# print(d["Asma"])
# print(d["dinesh"])


