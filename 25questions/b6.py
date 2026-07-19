#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
data=input("enter a sequence of comma-separated numbers: ")
numbers=data.split(",")# if this line is not present then it is showing number is not defined error
print("List:", numbers)     
print("Tuple:", tuple(numbers))