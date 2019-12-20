# Question no.1
# Define Object Oriented Programming Language?

# Object oriented programming is the characteristic of the programming language in which we can write our code by
# considering it as an object. Some of the object oriented programming languages are Python, Java, C++, C# and others

# Question no. 2
# List down the Benefits of OOP?

# 1- It provide a the definite structure in which the implementation details are hidden.
# 2- It makes the software or any program easy to maintain.
# 3- It increases the skills of the developer to think more by considering a object
# 4 - We can reuse of code through inheritance

# Question no. 3
# Differentiate between function and method?

# Function is creating a certain code with in the procedural oriented programming, which can do a certain work and we
# call a function where we want with in the code...
#
# Methods are similar as of function. The main difference is that methods are the function use within the class which
# can perform any action relating to the class attribute or anything else

# Question no. 4

# Define the following terms:
# 1. Class
# 2. Object
# 3. Attribute
# 4. Behavior

# 1- Class is the basic of the object oriented programming, Class is the blueprint for creating a object for our
#     further use
# 2- Object is the basic unit of object oriented programming in which a object can perform certain actions according to
#     program we are creating
# 3-  classes and objects have attributes. Attributes are data stored inside a class or instance and represent the state
#     or quality of the class or instance.
# 4- A class's Behaviour means how an instance of the class operates or behaves

# Question no. 5
# Write a code in python in which create a class named it Car which
# have 5 attributes such like (model, color and name etc.) and 3
# methods. And create 5 object instance from that class.


class cars:
    def __init__(self, name, color, model, owner, registration):
        self.name = name
        self.color = color
        self.model = model
        self.owner = owner
        self.registration = registration

        # class methods

    def update_color(self, new_color):
        self.color = new_color

    def update_model(self, new_model):
        self.model = new_model

    def update_owner(self, new_owner):
        self.owner = new_owner


# 1st instance
# car1 = cars("Civic", "Black", 2019, "Aaqib", "Yes")
# print(car1.__dict__)

# using method on 1st instance to change color

# car1.update_color = "Dark Blue"
# print(car1.__dict__)
# 2nd instance
# car2 = cars("Mercedes", "White", 2018, "Aaqib", "No")
# print(car2.__dict__)

# using method to change the model

# car2.update_model(2019)
# print(car2.__dict__)

# 3rd instance
# car3 = cars("Rolls Royce", "Red", "Phantom 2018", "Aaqib", "Yes")
# print(car3.__dict__)

# using the method to change the owner

# car3.update_owner("Asim")
# print(car3.__dict__)