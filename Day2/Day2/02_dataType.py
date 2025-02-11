# Data Type in Python

# 1) Numeric Data Type

# Integer (int): Whole numbers (positive or negative) without a decimal point

num1 = 19
num2 = -5
print("Integer:", num1, num2)


#Floating  Point (float): Real numbers with a decimal point

pi = 3.14
g = 9.8
print(type(pi))
print("Float:", pi, g)

# Complex: Numbers with a real and imaginary part

c = 2 + 3j
print(type(c))  # Output: <class 'complex'>
print(c.real)   # Output: 2.0
print(c.imag)   # Output: 3.0

x = 50
y = 10.5
z = 5 + 2j 


print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>


#----------------------------------------------------------------------------------------------------------------

# 2) Sequence Type

# String (str): A sequence of characters enclosed within single, double, or triple quotes

name = "Alishba"
greeting = 'Hello programmer'

print (name + " " + greeting)

name = "mariyam"
print("This is my Sister " + name)


# List: A collection of items separated by commas and enclosed within square brackets

collection = ["Apple", 1, "Mango"]
print("This is my " + str(collection[1]) + " " + collection[0] + " " "and"  + str(collection[2]))


food = ["biryani", "pizza", "burger", "pasta"]
print("I am very hungry i want " + str(food[0]) + ", " + str(food[1]) + ", " + str(food[2]))

fruits = ["Apple", "Banana", "Cherry"]
numbers = [1, 2, 3, 4, 5]

print(type(fruits))  # Output: <class 'list'>
print(fruits[1])     # Output: Banana

# List ko modify karna
fruits.append("Mango")  # Add new item
fruits[0] = "Orange"    # Change item

print(fruits)  # ['Orange', 'Banana', 'Cherry', 'Mango']



# Tuple: A collection of items separated by commas and enclosed within parentheses


color_tuple = ("Red", "Green", "Blue")
print (color_tuple[2])


#set: A collection of items separated by commas and enclosed within curly braces

set1 = {"Apple", "Banana", "Cherry" , "Apple" , "Banana"}

print(set1)  # Output: {'Apple', 'Banana', 'Cherry'}    

#--------------------------------------------------------------------------------------------------------------------


# mapping Type
# Dictionary: A collection of key-value pairs separated by commas and enclosed within curly braces

mySelf = {
    "name" : "Alishba",
    "age" : 20,
    "city" : "Karachi",
    "status" : "Web Developer",
    "height" : 5.2,
    "married" : False

}

print ("My name is " + mySelf["name"] + " and i am " + str(mySelf["age"]) + " years old" + " and i am from " + mySelf["city"] + " and i am a " + mySelf["status"] + " and my height is " + str(mySelf["height"]) + " and i am married " + str(mySelf["married"]))
#--------------------------------------------------------------------------------------------------------------------



#5. Boolean & None Types
is_python_fun = True
is_java_hard = False

print(type(is_python_fun))  # Output: <class 'bool'>
print(10 > 5)  # Output: True
print(10 == 5) # Output: False


# None: Represents the absence of a value
result = None
print(type(result))  # Output: <class 'NoneType'>
print(result)        # Output: None