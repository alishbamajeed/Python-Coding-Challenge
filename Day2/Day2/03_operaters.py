# Operators In Python

# Arithmetic Operators
# value ko add, subtract, multiply, divide, aur modulus karne ke liye use kiye jate hain

# Addition (+): Adds two operands
num1 = 10
num2 = 20
result = num1 + num2
print(result )  # Output: 30

# Subtraction (-): Subtracts the second operand from the first

result = num1 - num2
print(result )  # Output: -10

# Multiplication (*): Multiplies two operands
result = num1 * num2
print(result
)  # Output: 200

# Division (/): Divides the first operand by the second
result = num1 / num2
print(result )  # Output: 0.5

# Modulus (%): Returns the remainder when first operand is divided by the second
result = num1 % num2
print(result )  # Output: 10

# Exponent (**): Returns the first operand raised to the power of the second
result = num1 ** num2
print(result )  # Output: 100000000000000000000

# Floor Division (//): Returns the integer part of the division
result = num1 // num2

print(result )  # Output: 0

# Comparison Operators
# value ko compare karne ke liye use kiye jate hain

# Equal (==): Compares if the values of two operands are equal
num1 = 10
num2 = 20
result = num1 == num2
print(result )  # Output: False

# Not Equal (!=): Compares if the values of two operands are not equal

result = num1 != num2
print(result )  # Output: True

# Greater than (>): Compares if the value of left operand is greater than the value of right operand

result = num1 > num2
print(result )  # Output: False

# Less than (<): Compares if the value of left operand is less than the value of right operand
result = num1 < num2
print(result )  # Output: True

# Greater than or equal to (>=): Compares if the value of left operand is greater than or equal to the value of right operand

result = num1 >= num2
print(result )  # Output: False

# Less than or equal to (<=): Compares if the value of left operand is less than or equal to the value of right operand


result = num1 <= num2
print(result )  # Output: True

# Logical Operators

# Logical operators are used to combine conditional statements

# and: Returns True if both statements are true


e= True or False
print(e)

#Truth Table for AND Operator

print(True and True)  # Output: True
print(True and False)  # Output: False
print(False and True)  # Output: False
print(False and False)  # Output: False

#Truth Table for OR Operator

print(True or True)  # Output: True
print(True or False)  # Output: True
print(False or True)  # Output: True
print(False or False)  # Output: False

#Truth Table for NOT Operator

print(not True)  # Output: False
print(not False)  # Output: True

# and: Returns True if both statements are true

num1 = 10
num2 = 20
num3 = 30
result = num1 < num2 and num2 < num3
print(result )  # Output: True

# or: Returns True if one of the statements is true
result = num1 < num2 or num2 > num3
print(result )  # Output: True

# not: Reverse the result, returns False if the result is true
result = not(num1 < num2 and num2 < num3)


print(result )  # Output: False


# Assignment Operators

# Assignment operators are used to assign values to variables

# =: Assigns the value of the right operand to the left operand
d = 5==5
print(d)


num1 = 10
num2 = 20
num1 = num2
print(num1 )  # Output: 20

# +=: Adds the right operand to the left operand and assigns the result to the left operand
num1 = 10
num2 = 20
num1 += num2
print(num1 )  # Output: 30


# -=: Subtracts the right operand from the left operand and assigns the result to the left operand

num1 = 10
num2 = 20
num1 -= num2
print(num1 )  # Output: -10

# *=: Multiplies the right operand with the left operand and assigns the result to the left operand
num1 = 10
num2 = 20
num1 *= num2
print(num1 )  # Output: 200

# /=: Divides the left operand with the right operand and assigns the result to the left operand

num1 = 10
num2 = 20
num1 /= num2
print(num1 )  # Output: 0.5

# %=: Takes the modulus of the two operands and assigns the result to the left operand

num1 = 10
num2 = 20
num1 %= num2
print(num1 )  # Output: 10

# **=: Raises the left operand to the power of the right operand and assigns the result to the left operand

num1 = 10
num2 = 20
num1 **= num2
print(num1 )  # Output: 100000000000000000000

# //=: Performs floor division on the two operands and assigns the result to the left operand
num1 = 10
num2 = 20
num1 //= num2
print(num1 )  # Output: 0

# identity Operators

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

# is: Returns True if both variables are the same object

num1 = 10
num2 = 20

result = num1 is num2
print(result )  # Output: False

# is not: Returns True if both variables are not the same object
result = num1 is not num2
print(result )  # Output: True

# Membership Operators

# Membership operators are used to test if a sequence is presented in an object

# in: Returns True if a sequence with the specified value is present in the object

fruits = ["Apple", "Banana", "Cherry"]
result = "Apple" in fruits
print(result )  # Output: True

# not in: Returns True if a sequence with the specified value is not present in the object

result = "Mango" not in fruits

print(result )  # Output: True

# Bitwise Operators

# Bitwise operators are used to compare (binary) numbers

# & : AND: Sets each bit to 1 if both bits are 1

num1 = 10  # Binary: 1010
num2 = 20  # Binary: 10100
result = num1 & num2
print(result )  # Output: 0

# | : OR: Sets each bit to 1 if one of two bits is 1

result = num1 | num2
print(result )  # Output: 30


# ^ : XOR: Sets each bit to 1 if only one of two bits is 1

result = num1 ^ num2

print(result )  # Output: 30

# ~ : NOT: Inverts all the bits

result = ~num1

print(result )  # Output: -11

# << : Zero fill left shift: Shift left by pushing zeros in from the right and let the leftmost bits fall

result = num1 << 2

print(result )  # Output: 40

# >> : Signed right shift: Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall

result = num1 >> 2

print(result )  # Output: 2

#--------------------------------------------------------------------------------------------------------------------

