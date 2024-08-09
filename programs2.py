from functools import reduce
l = ["1", "13", "143", "21"]


def square(a):
    return int(a) * 2


print(list(map(square, l)))


# wap to find the biggest number among given number
s = "10, 20, 34, 78"
max = 0
for num in s.split(','):
    if max < int(num):
        max = int(num)
print(max)

x = '12345'
y = 'abc'
output = ""
for i in range(len(x)):
    if i < len(y):
        output += x[i] + y[i]
    else:
        output += x[i]
print(output)


# wap to print the second largest number in the list of tuples
t = [(8, 9), (9, 1), (2, 8), (-2, 18), (7, 11)]
maxx = t[0][1]
# print(maxx)
op = ()
for value in t:
    # print(value[0])
    if value[1] > maxx:
        maxx = value[1]
        op = value
print(op)


for i in range(2, 101):
    for j in range(2, 101):
        if i % j == 0:
            break
    if i == j:
        print(i, end=" ")
        print(i, "is a prime number")


x = '12345'
y = 'abc'
op = ""
for i in range(len(x)):
    if i < len(y):
        op += x[i] + y[i]
    else:
        op += x[i]
print(op)


s = "abc"
s1 = "12345"
op = ""
for i in range(len(s)):
    if i < len(s1):
        op += s[i] + s1[i]
print(op + s1[3::])


a = int(input("Enter a number"))
word = ["sun", "mon", "tue"]
flag = 0
for i in range(1, a):
    if i % 3 == 0:
        print(word[flag])
        flag = flag + 1
    else:
        print(i)
        if flag == 3:
            flag = 0
x = '3a2b1c4d'
op = ""
for i in range(0, len(x), 2):
    op += x[i] * int(x[i])
print(op)

s = "3a2b1c4d"
op = ""
for i in range(0, len(x), 2):
    op += x[i+1] * int(x[i])
print(op)


y = "aaaabbbccd"
res = ""
count = 1
for i in range(1, len(y)):
    if y[i] == y[i-1]:
        count += 1
    else:
        res += y[i-1] + str(count)
        count = 1
res += y[-1] + str(count)
print(res)


data = """name age salary location
yeswanth  23  34598  bangalore
bharath   20  12330  chennai
akhil     26  34598  bangalore
hari      27  12330  chennai"""

line = data.split("\n")[1:]
d = {}
for row in line:
    # print(row)
    name, age, salary, location = row.split()
    d[name] = {"age": int(age), "salary": int(salary), "location": location}
print(d)


# wap to concatinte list of words using reduce and lambda
l = ["Hi", "Hello", "world"]
print(reduce(lambda a, b: a + " " + b, l))


# write a program to print the word which contains "o" in list

l = ["Hi", "Hello", "world"]
result = [i for i in l if "o" in i]
print(result)

data = "Hi 1,hello2.welcome$ 456"
op = []
consonants = []
digits = []
special_char = []
for i in data:
    if i in "aeiou":
        op.append(i)
    elif i not in "aeiou" and i.isalpha():
        consonants.append(i)
    elif i.isdigit():
        digits.append(i)
    else:
        special_char.append(i)
print(op, special_char, consonants, digits)


# wap to print the consecutive numbers and sum of them
s = "welcomeHi 12 Hello45  6 whats 78 up 11"
add = 0
sub = ""
for i in s:
    if i.isdigit():
        sub += i
    else:
        if sub:
            add += int(sub)
            sub = ""
add += int(sub)
print(add)
