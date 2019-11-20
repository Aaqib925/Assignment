# question no. 1


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("1. Addition.")
print("2. Subtraction.")
print("3. Multiplication.")
print("4. division.")
print("5. Power.")
while True:
    choice = int(input("Enter the number for which operation you want to do: "))

    if choice == 1:
        print(x, "+", y, "=", x + y)

    elif choice == 2:
        print(x, "-", y, "=", x - y)

    elif choice == 3:
        print(x, "*", y, "=", x * y)

    elif choice == 4:
        print(x, "/", y, "=", x / y)

    elif choice == 5:
        print(pow(x, y))

    else:
        print("Please select correct choice.")


# question no. 2

my_list = [1, 2, 3, 4, 5]

x = int(input("Which element you want to find in this list? "))
for i in my_list:
    if i == x:
        print("The element exist.")



# question no. 3

dictionary = {"name": "Aaqib", "father name": "Nazir", }

dictionary["Roll_number"] = "CT-47"
print(dictionary)



# question no. 4


sum_ = 0
dictionary = {"a": 1, "b": 2, "c": 3}
for i in dictionary:
    sum_ += dictionary[i]
print(sum_)



# question no. 5


m_list = [1, 2, 3, 5, 6, 4, 2, 1]


def func(my_list):
    repeated_values = []
    length = len(my_list)
    for i in range(length):
        for j in range(i + 1, length):
            if my_list[i] == my_list[j] and my_list[i] not in repeated_values:
                repeated_values.append(my_list[i])
    return repeated_values


print(func(m_list))


# question no. 6

key1 = input("which key you want of find: ")

dic = {"name": "Aaqib", "father name": "Nazir", "age": 15}


def check_keys(dictionary, key):
    """ a function which find if the key is repeated or not """
    if key in dictionary.keys():
        print("The key {} is present".format(key))
    else:
        print("The key {} is not present".format(key))

check_keys(dic, key1
