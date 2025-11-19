#interpretor vs code terminal

#print("Welcome to python programming")
#print("Hello World")

# print("hello world".upper())


#print(2)
#print (3.5)


# string, integer, float, boolean  ( anything in # hash is not going to be run(excuted), this is comment.)


# list is also another data type( anything in a square braket[  ]

#print(type(y))



# variables can not start with numbers
# variables must be alphanumeric( A-Z, 0-9) MUST START WITH LETTER OR UNDERSCROLL_
# variables are case sensetive
# variables must not be reserved word( like , if, or, false, true , and)

# print(18/4)
# print(5 ** 2)
# print(18 % 4)


# sentence = "Python is fun and interesting"
# Concat_str = sentence [:3] + sentence [-3:]
# print("Concatenated string:", concat_str)
# upper_str = concat_str.upper()
# print ("uppercase string:", upper_str)
# repeated_str = upper_str * 2
# print("repeated string:", repeated_str)
# substring = sentense [4:10]
# print ("Substring (5th to 10th):"

####activity2

# print(18/4)
# print(5 ** 2)
# print(18 % 4)


#######
 
# name = "Selam"
# age = 27
# hobby = "pickleball"
# favorite_animal = "cat"

# print("my name is  " + Selam + ", I am  " + str(27) + " years old, my hobby is  "+ pickleball + ", and my favorite animal is a  " + cat + ".")

#  sentence
# sentence = "Python is interesting"

# 1. Concatenate the first 3 chars with the last 3 chars
# concat = sentence[:3] + sentence[-3:]
# print("Concatenated:", concat)

# # 2. Convert to uppercase
# upper_concat = concat.upper()
# print("Uppercase:", upper_concat)

# # 3. Repeat the uppercase string two times
# repeated = upper_concat * 2
# print("Repeated:", repeated)

# # 4. Extract substring from 5th to 10th character (inclusive)
# substring = repeated[4:10]
# print("Substring (5th to 10th):", substring)

# # 5. Convert each word in the original sentence to lowercase
# words = sentence.lower().split()
# print("Lowercase words:", words)

# # 6. Print the modified list of words along with its length
# print("Number of words:", len(words))

#step-by-step output

# Step-by-Step Output
# 	1.	Concatenate first 3 + last 3:
# Pyting
# 	2.	Convert to uppercase:
# PYTING
# 	3.	Repeat two times:
# PYTINGPYTING
# 	4.	Substring from 5th to 10th (inclusive):
# 👉 Remember Python counts from 0, so this takes characters 4 → 9
# NGPYTI
# 	5.	Lowercase words:
# ['python', 'is', 'interesting']
# 	6.	Length of list:
# 3

# Final output

#Concatenated: Pyting
# Uppercase: PYTING
# Repeated: PYTINGPYTING
# Substring (5th to 10th): NGPYTI
# Lowercase words: ['python', 'is', 'interesting']
# Number of words: 3

# x = "Hello"
# print(type(x))

# a = 10
# b = 5
# print(10 % 5)

# a = "5"
# b = "10"
# print(a + b)

# f = 10
# g = 10
# h = 10
# f = g = h
# print(f, g, h) 

# print(18/4)
# print(5**2)
# print(18%4)

# fname = "abebe"
# lname = "kebede"
# print(fname + lname)

# name = "abebe"
# lname = "kebede"
# print(fname + " " + lname)

# #if we want to code the following, it will be

# age = 20
# name = "abebe"
# print("my name is " + "abebe " + "and i am " + str(20) + " years old ")

# # if we want to print z as a string 
# z = 20
# print(str(z))
# print(type(str(z)))

# s = str(123)
# print(s)

### redo this
# name = "abdi"
# age = 30
# Hobby = "reading books"
# Favorite_animal = "dog" 

# print("My name is abdi, I am 30 years old, my hobby is reading book, and my favorite animal is a dog.")

# fname = "Almaz"
# lname = "Abebe"
# print("Almaz" " Abebe")

#
#Str1 = "Hello"
# print(Str1 * 3)
# result = Str1 * 3

# str1 = "python"
# print(str1[0])
# print(str1[2])

# str1 = "Hello, World!"
# mylength = len(str1)
# print(len(str1))
# print(mylength)
# print(str1.upper())



##1.concatenate the first three characters of the sentence with the last three characters
# first create a sentence, then concatenate the first three using the operation slicing
# last three is counting from back ward, thats going to be a -ve valuse, the ending letter is -1 then 12....


# mysentence = "python is fun"
# firstThree = mysentence[:3]
# lastThree = mysentence[-3:]
# concatenatedString = firstThree + lastThree
# print(concatenatedString)
# #2.convertconcatenated string to uppercase
# upperstring = concatenatedString.upper()
# print(upperstring)
# #Repeat the upper string two times
# repeatedstring = upperstring * 2
# print(repeatedstring)
# #Extract the substring from the 5th to 10th character(inclusive) from the repeated string
# substring = repeatedstring{4:10}
# print(substring)
# #convert each word to lower case
# lowersubstring = substring.lower()
# print(lowersubstring)
# #print the modified list of lowercase words along with its length
# mylist = lowersubstring.split(2)


# a = 4
# b = 3
# a ==

# Activity1
# colors = {"Yellow", "Orange", "Black"}
# print(colors)
# colors.update(["purple", "green","white"])
# print(colors)
# colors.remove("Orange")
# print(colors)

# activity2
# setA = {"Yellow", "Orange", "Black"}
# setB = {"Black", "Blue", "Yellow"}
# union_set = setA.union(setB)
# print("union:", union_set)

# setA.intersection_update(setB)
# print("Intersection(updated setA):", setA)

# setA = {"Yellow", "Orange", "Black"}
# diff_set = setA.difference(setB)
# print("Difference ( A - B ):", diff_set)

# activity3
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10,20,30]
# my_dict = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# print(my_dict)

# activity4
# dict1 = {'Ten': 10, 'Twenty': 20, "Thirty": 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)


# num = int(input("Enter a number: "))
# print("you entered: ", num)
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero") 

 #while loop
# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello Geek")

# count = 0
# while ( count < 5):
#     print("count is:", count)
#     if count == 3:
#         break
#     count += 1

# for i in range(3):
#     print("* * *")
# for i in range(1, 5):
#     print(("* " * i).rstrip()) 


#activity
# word = input("enter a word: ")
# for letter in word: 
#     print(letter)


# total = 0
# for num in range(1,11):
#     total += num
#     print("the sum 1 to 10;", total) 

# total = 0
# for num in range(2,11):
#     if num % 2 == 0:
#         print(num) 

# password = "python1234"
# cpassword = input(" enter correct password: ")
# while password != cpassword:           #!= > not equal to
#     print("incorecct password")
#     password = input("enter correct password: ") 
#     print("success")
 

