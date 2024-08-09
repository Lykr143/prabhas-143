"""
Decorators:
-----------
Decorators are wrapper function in python which are used implement
additional functionality without disturbing base function

To use the specific decorator mention @decorator_name on top of the base function


when we try to execute the base function, python will call decorator function
 and decorator will call  base function"""

# 3.Decorator called function


def check_type(fun):  # fun = add
    # 5.wrapper called function
    def wrapper(a, b):
        if type(a) == int and type(b) == int:
            # base function calling function
            return fun(a, b)
        else:
            return "both values should be integers"

    # 4.wrapper calling function
    # This is the calling function of Wrapper called function
    return wrapper  # calling function

# 2.decorator calling function


@check_type
# base function called function
def add(a, b):
    return a + b


# 1base function calling function
print(add(10, 20))  # 1
print(add(10, "23"))
print(add(10, [1, 23]))


# write a decorator to print the city names(strings) only
def city_names(name):  # name = get_city_names
    def wrapper(names):
        op = []
        for i in names:
            if type(i) == str:
                op.append(i)
        return name(op)

    return wrapper


@city_names
def get_city_names(names):
    print(names)


get_city_names([1, 2, "hyd", "bang"])


# write a decorator which prints the square of the elements of the list
def square(n):  # n = print_list
    def wrapper(l):
        op = [i * i for i in l]
        return n(op)
    return wrapper


@square
def print_list(l):
    print(l)


print_list([2, 3, 4, 5])

# wap to swap two numbers without using third variable and multivariable assignement

a = 10
b = 20
b = a + b
a = b - a
b = b - a
print(a, b)

# wap to find the biggest among multiple numbers which are in a string and seperated by ,
s = "25,65,107,78,98"
maxx = 0
for num in s.split(","):
    if maxx < int(num):
        maxx = int(num)
print(maxx)


# wap to check the given character is a vowel or consonant
def check_vowels(string):
    for i in string:
        if i in "aeiouAEIOU":
            print(i, "is a vowel")
        else:
            print(i, "is a consonants")


check_vowels("h")
check_vowels("a")
check_vowels("A")
check_vowels("s")

# wap to find the largest number in the given list
l = [23, 34, 90, 56, 89, 18, 108, 68]
maxx = l[0]
for i in l:
    if maxx < i:
        maxx = i
print(maxx)


# wap to print the elements which are divisible by 3, 5 and both
value = [3, 5, 7, 11, 9, 15, 30, 25]
op = []
for num in value:
    if num % 3 == 0 and num % 5 == 0:
        op.append(num)
print(op)

result = [num for num in value if num % 3 == 0 and num % 5 == 0]
print(result)


# wap to print sum of adjacent elements
l = [3, 5, 7, 11, 15, 30]
#[8, 12, 18, 26, 45]
op = []  # empty list which is used to store the output
for i in range(len(l)-1):  # iterate through each element upto last element
    add = l[i] + l[i + 1]
    op.append(add)
print(op)


# wap to reverse a list without slicing or reverse function
l = [6, 4, 2, 5, 1]
print([l.insert(0, i) for i in l])
#1, 5, 2, 4, 6,
