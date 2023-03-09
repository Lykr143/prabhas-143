# x = 100
# y = 5
# print(a//b*a/b)

# a = [0,1,5,9]
# for a[-1] in a:
# 	print(a[-1])

# a = input("enter your name:")
# print(a*5)

# a = [int(x) for x in input("enter number:").split(',')]
# print(a)

# b = (range(6))
# sum = 0
# for i in b:
# 	sum = sum+i
# print(sum)
	

'''# = [int(x) for x in input("enter a numbers:").split(',')]
a = [int(x) for x in input("enter number:").split(',')]
e_sum = 0
o_sum = 0
even = []
odd = []
for i in a:
	if i%2==0:
		even.append(i)


		e_sum = e_sum+i


	else:
		odd.append(i)
		o_sum  = o_sum+i

print(e_sum)
print(o_sum)

print(even)
print(odd)'''

'''a = int(input("enter a number:"))
for i in range(1,11):
	print(a, "*", i, "=", a*i)'''
'''a = [1,2,3,5,7,6]
e_sum = 0
o_sum = 0
even = []
odd =[]

for i in a:
	if i%2 == 0:
		even.append(i)
		e_sum = e_sum+i
	else:
		odd.append(i)
		o_sum = o_sum+i 
print(e_sum)
print(o_sum)		
print(even)
print(odd)'''

# a = int(input("enter a number:"))

# for i in range(1,11):
# 	print(a, "*", i, "=", a*i)




#a = [int(x) for x in input("enter number:").split(",")]
'''a = [int(x) for x in input("enter number:").split(',')]
sum = 0
for i in a:
	sum = sum+i
print(sum)'''

		


'''a =  int(input("enter a num:"))
b = int(input("enter another number:"))
for i in range(a,b):
	print("mutiplication table for :",i)
	for j in range(1,11):
		print(i, "*", j, "=", i*j)'''


'''for i in range(10,16):
	print("mutiplication table for :",i)
	for j in range(1,11):
		print(i, "*", j, "=", i*j)'''

'''s = "yeswanth124"
for char in s:
	if not(char.isalpha() and char.islower()):
		print("invalid")
		break
	else:
		print(char)    
print("done")'''

# l = [1,2,3,4,5]
# for i in l:
# 	print(i * i)
# 	print(i * i * i)
# 	continue
# 	print("done")


# l = [1,2,3,4,5]
# e_sum = 0
# o_sum = 0
# for i in l:
# 	if i%2 == 0:
# 		e_sum = e_sum + i
# 	else:
# 		o_sum = o_sum + i
# print(o_sum - e_sum)

'''a,b,c,d,e,f = [1,2,3,4,5,6]
a,b = b,a
c,d = d,c
e,f = f,e

print(a,b,c,d,e,f)'''

# l= [1,0,1,0,1,0]
# j = 0
# for i in range(len(l)):
# 	if l[i] != 0:
# 		l[j],l[i] = l[i],l[j]
# 		j = j+1
# print(l)
# l = [1,2,3,4,5,6]
# length = len(nums)
# for i in range (len(0,length)):
# 	if i+2<length:
# 		numbers[i],numbers[i+2] = numers[i+2], numbers[i]
# 	if i+3<length:
# 		numbers[i+1],numbers[i+3] = numbers[i+3],numbers[i+1]
# 		retuns
# print(l)		



'''for i in range(10,20):
	print("multiplication table for:",i)
	for j in range(1,11):
		print(i, "*", j, "=", i*j)'''



'''l = [1,2,3,4,5,6]
for i in range(0, len(l), 2):
	l[i], l[i+1] = l[i+1], l[i]
print(l)'''


# l = [1,2,3,4,5,6]
# for i in range (0, len(l), 2):
# 	l[i], l[i+1] = l[i+1], l[i]
# print(l)	

'''i = 1
while i < 6:
	print(i)
	i = i + 1'''
a = [1,2,3,4,5,6]
i = 0
while i < len(a):
	a[i], a[i+1] = a[i+1], a[i]
	i = i + 2
print(a)	

# l = [1,3,5,0,6,0,7,0]
# j = 0
# for i in range (len(l)):
# 	if l[i] != 0:
# 		l[j],l[i] = l[i],l[j]
# 		j = j + 1
# print(l)		
'''l = [1,2,1,3,2,2,1]
l1 = []
for i in range(len(l)):
	for j in range(i+1,len(l)):
		if(l[i] == l[j]):
			l1.append(l[j])
print(list(set(l1)))'''

# l = [1,2,1,3,2,2,1]
# l1 = set(l)
# print(l1)

'''l1 = [1,2,3]
l2 = [4,5,6]
l3 = []
for i in range(len(l1)):
	add = l1[i] + l2[i]
	l3.append(add)
print(l3)'''
# def multiplication (n, d):
# 	return n*d
# print(multiplication(10, 3))
# print(multiplication(10, 2))

'''d = { "test1": { "age" : 23, "salary" : 50000, "ded" : 600 },
      "test2" : { "age" : 34, "salary" : 14000, "ded" : 500 }}
def total_emp_salary(d):
	total = 0
	for i in d:
		total += d[i]["salary"] + d[i]["ded"]
	return total
print(total_emp_salary(d))'''

# def total_age(d):
# 	total = 0
# 	for i in d:
# 		total += d[i]["age"]
# 	return total
# print(total_age(d))		


# l = [1,2,3,4,2,3,2,3,2]
# d = {}
# for i in l:
# 	d[i] = l.count(i)
# print(d)	

# def sub(a,b):
# 	c = a - b
# 	print("sub =", c)
# def add(a,b):
# 	c = a + b
# 	print('add =', c)

	
'''l = [1,2,3,4,]
def ele(l):
	for i in l:
		if i%2 == 0:
			yield i'''
'''l = [1,2,3,4,5]
x = iter(l)
print(x)
print(next(x))
print(next(x))
print("done")
for i in x:
	print(i)'''

# a = 10
# b = 20
# try:
# 	c = a/b
# 	print(c)
# except Exception as e:
# 	print(str(e))
# finally:


# fp = open("C:/Users/Yeswanth/Desktop/Manohar dpocs/data.txt", 'a')
# fp.write('hi\n')
# fp.writelines(['hello\n', 'yeswanth\n'])
# fp = open("C:/Users/Yeswanth/Desktop/Manohar dpocs/data.txt", 'r')
# print(fp.read())

# # def add (a,b=0,c=0):
# 	return (a+b+c)
# print(add (10))
# print(add(10,20))
# print(add(10,20,30))	

# def test (*a):
# 	return (a)
# print (test ())
# print(test(1,2,345))	

# def test (a,b=0,*c):
# 	return (a,b,c)
# print(test(10))
# print(test(10,20,30))
# print(test(10,20,30,40,50,60))

# def test (**d):
# 	return d
# print(test(a = 10))	
# print(test(a =10, b =20, c =48))



'''def test (a,b = 0, *c, **d):
	return (a,b,c,d)
print(test(10))
print(test(10,20,30))
print(test(10,20,30,40,50,60,70, x = 80, y = 90))

l = [1,2,3,3,4,5,5,5,7,2]
d = {}
for i in l:
	d[i] = l.count(i)
print(d)'''





	



	
	