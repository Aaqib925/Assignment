# question no. 1

my_dict = {"first_name": "Aaqib", "last_name": "Nazir", "age": 18, "city": "Karachi"}

# print(my_dict.items())

my_dict["qualification"] = "Intermediate"

my_dict.update({"qualification": "Higher education"})

del my_dict["qualification"]
print(my_dict)

# question no. 2

cities = {"karachi": {"country": "Pakistan", "population": "14.91 million", "fact": "Sea harbour"},
          "Islamabad": {"country": "Pakistan", "population": "1.015 million", "fact": "Capital"},
          "lahore": {"country": "Pakistan", "population": "11.13 million ", "fact": "Lahore lahore ay"}
          }

print(cities)

# question no. 3

num_of_persons = int(input("Write how many people want tickets: "))

total2 = []
for i in range(num_of_persons):
    total = 0
    age = int(input("Enter the age: "))
    if age > 3:
        total += 0
    if 3 <= age <= 12:
        total += 10
    if age > 12:
        total += 15
    total2.append(total)

print("Your total cost of ticket is: ", str(sum(total2)) + "$")


# question no. 4

#
def favorite_function(title):
    print("The tittle of your book is:", title)


my_title = input("Enter the title of the book: ")

favorite_function(my_title)

# question no. 5

import random

random_number = random.randint(1, 30)
print(random_number)

for i in range(3):
    user_guess = int(input("Enter to guess the number: "))

    if user_guess > random_number:
        print("Your number was greater than the number generated by me.")
    elif user_guess < random_number:
        print("Your number was lesser than the number generated by me.")
    elif user_guess == random_number:
        print("Great!! You guessed right number.")
