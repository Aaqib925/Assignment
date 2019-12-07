# Question 1
# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.


# def fact(num):
#     """ functions which finds a factorial value of the number """
#     factorial = 1
#     if num < 0:
#         return "The factorial of the negative number doesn't exist."
#     elif num == 0 or num == 1:
#         return "The factorial of {} is 1".format(num)
#
#     elif num > 1:
#         for i in range(1, num + 1):
#             factorial = factorial * i
#
#     return factorial
#
#
# number = int(input("Enter the number you want to find the factorial: "))
#
# print("The factorial of {} is:".format(number), fact(number))

# Question:2
# Write a Python function that accepts a string and calculate the number of upper
# case letters and lower case letters.

# sent = input("Enter the String: ")
# lower_letters = "abcdefghijklmnopqrstuvwxyz"
# upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# upper_count = 0
# lower_count = 0
# for i in sent:
#     if i in lower_letters:
#         lower_count += 1
#     elif i in upper_letters:
#         upper_count += 1
# print("The number of upper case letters are: ", upper_count)
# print("The number of lower case letters are: ", lower_count)

Question:3
Write a Python function to print the even numbers from a given list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []
for i in lst:
    if i % 2 == 0:
        even_numbers.append(i)

print("The even numbers in given lists are:", even_numbers)

Question:4
Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same
backward as forward, e.g., madam

word = input("Enter any word: ")
reverse_word = word[-1::-1]
if word == reverse_word:
    print("The word {} is palindrome".format(word))
else:
    print("The word {} is not palindrome".format(word))

Question:5
Write a Python function that takes a number as a parameter and check the
number is prime or not.

def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("The number {} is not prime number".format(num))
                print(str(i), "*", str(num // i), "=", num)
                break
        else:
            print("The number {} is a prime number".format(num))


number = int(input("Enter any number: "))
prime(number)

Question: 6
Suppose a customer is shopping in a market and you need to print all the items
which user bought from market.
Write a function which accepts the multiple arguments of user shopping list and
print all the items which user bought from market.

def items(*names):
    """ This functions accept multiple argument and print it """
    print("The items customer bought are as follows: ")
    for item in names:
        print(item)

items("Chocolate", "Mango juice", "Vegetables")