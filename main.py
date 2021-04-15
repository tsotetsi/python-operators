# Task 1 Sample solution
# Given two sides of right angled triangle
# Calculate the third side. Get two sides from
# the user.

ab = float(input("Please enter the first side: "))
bc = float(input("Please enter the second side: "))

ac = (ab**2 + bc**2)**(1/2)
print("The third side of the triangle equals: "+ str(ac))

# Task 2
# Given a list, find the max number and min number.
my_list = [2, 56, 12, 67, 1000, 32, 89, 29, 44, 39, 200, 11, 21]
print("Max number in my_list is: " + str(max(my_list)))
print("Min number in my_list is: " +str(min(my_list)))
