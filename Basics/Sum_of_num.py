x = int(input("Enter first number: "))  # Always takes a string value by default
print(type(x))  # displays the type of datatype
y = int(input("Enter the second number: "))
z = str(x + y)  # z is now a string
print("The sum of the numbers = " + z)  # only string can be concatenated with a string
