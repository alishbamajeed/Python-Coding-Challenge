# Loops in Python
# for variable in sequence:
    # Code jo bar bar chalega


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)


for i in range(5):  # 0 se 4 tak loop chalega
    print("Hello, Python!")


for i in range(1, 10, 2):  # 1 se start, 10 se pehle tak, har bar 2 increment
    print(i)




#while loop (Condition-Based Loop)

#while condition:
    # Code jo bar bar chalega


count = 1
while count <= 5:
    print(count)
    count += 1  # count = count + 1


#Infinite Loop (Endless Loop)


while True:
    print("Alishba")

#break and continue in Loops

for i in range(10):
    if i == 5:
        break  # Loop yahan ruk jayega
    print(i)


#Nested Loops (Loop ke andar Loop)

for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")


#else with Loops

for i in range(3):
    print(i)
else:
    print("Loop complete!")



#(Loop with break, continue, and else)

for i in range(5):
    if i == 2:
        continue  # Skip `i=2`
    if i == 4:
        break  # Stop loop at `i=4`
    print(i)
else:
    print("Loop completed!")  # This won't execute because of `break`
