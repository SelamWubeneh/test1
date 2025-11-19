#ACTIVITY
# Concatenate the first three characters of the sentence with the last three characters of the sentence.

# sentence = "python is fun"
# first_three =sentence[:3]
# last_three = sentence[-3:]
# concatenatemystring = first_three + last_three 
# print(concatenatemystring)


# # Convert the concatenated string to uppercase.
# result = concatenatemystring.upper()
# print(result)

# # Repeat the uppercase string two times.

# result = concatenatemystring.upper() * 2
# print(result)

# # Extract the substring from the 5th to the 10th character (inclusive) from the repeated string.
# result = concatenatemystring [4:10]
# print(result)


# # Convert each word to lowercase.
# lowerresult = result.lower()
# print(lowerresult)

# # Print the modified list of lowercase words along with its length.
# wordlist = lowerresult.split()
# print(wordlist)
# print(" number of words: ", len(wordlist))



#ACTIVITY---------------------------------

# Write a Python program that determines the price of a movie ticket based on age and whether the person is a student.
# If the person is 18 or older:
# If they are a student, the ticket price is $10.
# Otherwise, the ticket price is $15.
# If the person is under 18:
# If they are a student, the ticket price is $8.
# Otherwise, the ticket price is $12.

# how to solve this?
# 1. ask the user for thier age and student status 2. determine ticket price. 3. display result.

# age = int(input("Enter your age: "))
# isstudent = input("Are you a student? (yes or no): ").lower()

# if age >= 18 and isstudent == "yes": 
#     price = 10
# elif age >= 18 and isstudent == "no":
#     price = 15
# elif age < 18 and isstudent == "yes":
#     price = 8
# else:
#     price = 12
# print(" The movie ticket price is " + str(price))






















#1 Ask the user to input a sentence and count how many words it contains. Assume a word is separated by exactly one space.
# sentence = input("Enter a sentence: ")
# word = sentence.split()
# count = len(word)
# print("number of words:", count)

#2. Write a program that takes a word as input and asks the user how many times they want the word to be repeated. Then, the program should print the word that many times, with each repetition separated by a space, all on the same line.
#       Example
#               Enter a word: hello
#               How many times would you like it repeated? 3
#               hello hello hello

# word = input("Enter a word: ")
# repeat = int(input("how many times to repeat? "))
# result = (word + " ") * 3
# print(result)

# 3. Write a program that counts how many vowels are in a given string. Make sure to get the string from the user
# word = input("Enter a word: ")
# vowels = "aeiouAEIOU"  # includes both lowercase and uppercase vowels
# count = 0
# for letter in word:
#     if letter in vowels:
#         count += 1
# print("Number of vowels:", count)

# 4. Ask the user to input a password. Print whether it is "Weak", "Medium", or "Strong" based on the following rules:
#     Weak: Less than 6 characters
#     Medium: 6-10 characters, only letters
#     Strong: More than 10 characters and contains letters and numbers

# password = input("Enter your password: ")
# if len(password) < 6:
#     print("Password is Weak")
# elif len(password) <= 10 and password.isalpha():
#     print("Password is Medium")
# elif len(password) > 10 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
#     print("Password is Strong")
# else:
#     print("Password does not meet the criteria")
# 5.  Write a program that prints numbers from 1 to 50, but:
#            If the number is divisible by both 3 and 5, print "FizzBuzz"
#            If divisible by only 3, print "Fizz"
#            If divisible by only 5, print "Buzz"
#           Otherwise, print the number
# for num in range(1, 51): # from one to 51 is range, we want 50 to be included so we use 51
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# 6. Write a program that calculates the sum of numbers in a range, but:
#      - Ask user for start and end numbers
#      - Skip numbers divisible by 4
#      - Stop adding if sum exceeds 100
    #  - Print each number being added
# Ask user for start and end numbers #basically the question is asking pick a number range like 0 and keep adding to the next range 0+1+2+3.. 
# but skip if it is divisible by 4 for this case 4,8,12 are divisible by 4 ...but stop when adding these numbers start exceeding 100
#so py will keep adding the number up to 15 because once you reach 15 the number will exceed 100 1-15(96). so start nuber is 0 end number can be 15

# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))

# total = 0  # to keep track of the running sum

# for num in range(start, end + 1):  # loop through the range
#     if num % 4 == 0:       # skip numbers divisible by 4
#         continue
    
#     if total + num > 100:  # stop if sum exceeds 100
#         print("Sum would exceed 100. Stopping.")
#         break
    
#     total += num           # add number to total
#     print("Adding:", num)  # show each number being added

# print("Final sum:", total)

# 7.  Write a program that calculates a student's final grade based on:
#      If attendance is below 75%, automatic F
#          Otherwise, if score >= 90: A
#          If score >= 80: Check if attendance >= 90% for A-, else B+
#          If score >= 70: C
#          If score >= 60: D
#          Below 60: F

# attendance = float(input("Enter attendance percentage: "))
# score = float(input("Enter exam score: "))

# if attendance < 75:
#     print("Final Grade: F (Attendance below 75%)")

# else:
#     if score >= 90:
#         print("Final Grade: A")
#     elif score >= 80:
#         if attendance >= 90:
#             print("Final Grade: A-")
#         else:
#             print("Final Grade: B+")
#     elif score >= 70:
#         print("Final Grade: C")
#     elif score >= 60:
#         print("Final Grade: D")
#     else:
#         print("Final Grade: F")

# 8. Write a program that converts temperature between Celsius and Fahrenheit. Ask the user which conversion they want (C to F or F to C), then ask for the temperature. If they enter an invalid choice, keep asking until valid.
# Formulas:
# F = (C × 9/5) + 32
# C = (F - 32) × 5/9
# 9. Write a program that takes a sentence as input and replaces all vowels (a, e, i, o, u) with asterisks (*). Keep the case of other letters unchanged.
# Example Input: "Hello World"
# Example Output: "H*ll* W*rld"

# sentence = input("Enter a sentence: ")
# vowels = "aeiouAEIOU"   # all vowels, lowercase + uppercase
# result = ""              # empty string to build the new sentence

# for char in sentence:
#     if char in vowels:   # check if each letter is a vowel
#         result += "*"    # replace vowel with asterisk
#     else:
#         result += char   # keep consonants and other characters the same

# print("Modified sentence:", result)



# 10. Write a program that asks the user to enter numbers one by one. If the user enters a negative number, stop asking and print the sum of all positive numbers entered.
# Example Output:
# Enter a number: 5
# Enter a number: 10
# Enter a number: 3
# Enter a number: -2
# Sum of positive numbers: 18 


# total = 0  # keeps track of the sum

# while True:  # loop runs forever until we break it
#     num = int(input("Enter a number: "))
    
#     if num < 0:
#         break   # stop asking when a negative number is entered
    
#     total += num  # add the positive number to the total

# print("Sum of positive numbers:", total)


#loop
#question: print the numbers from 1 to 10(inclusive), one per line.
 
# for i in range(1, 11):     #11 is excluded but 10 is included
#     print(i)

# Ask the user for N and show the total of 1 to N.

# N = int(input("enter N: "))
# total = 0

#Sum from 1 to N
#Question: Ask the user for N and show the total of 1 to N.

# N = int(input("Enter N: "))
# total = 0
# for i in range(1, N+1):
#     total += i

# print("str1 " + "str2")