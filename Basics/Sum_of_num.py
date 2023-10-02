x = input("Enter first number: ") #Always takes a string value by default
print(type(x)) # displays the type ofd datatype
a = int(x) # typecasted to int
y = input("Enter the second number: ")
b = int(y)
z = a + b # z is now an int
ans = str(z) # typecasted to string since we can concatenate string with str only
print("The sum of the numbers = " + ans)
