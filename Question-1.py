# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# sample input: 10
# sample output: 35


# Solution
Input = int(input('sample input:', ))
Func = (lambda x : x + 25)
print ('sample output:', (Func(Input)))

