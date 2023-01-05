# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:[16, 25, 4, 81]

# Solution
Sample_list = [4,5,2,9]
Func = map(lambda x : x**2, Sample_list)
print ('Square the elements of the list: ', list(Func))
