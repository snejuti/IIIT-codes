students={
    "name": input("Enter the name of the student: "),
    "age": input("Enter the age of the student: "),
    "grade": input("Enter the grade of the student: ")
}
students["city"]=input("Enter the city of the student: ") #adding a new key-value pair to the dictionary
print(students)#print the dictionary
#print(students["name"],students["city"])#accessing the value of a key
students.update({"age": input("Enter the new age of the student: ")})#updating the value of a key
#loop through the dictionary
for key, value in students.items():
    print(key, value)

# for this we have to go to terminal and write python Q2(secondform).py to run the code and input the required values.