#in normal form giving the values already
students={
    "name":"SONIA",
    "age": 20,
    "grade": "A"
}
students["city"]="Delhi" #adding a new key-value pair to the dictionary
print(students)#print the dictionary
#print(students["name"],students["city"])#accessing the value of a key
students.update({"age": 21})#updating the value of a key
#loop through the dictionary
for key in students:
    print(key,students[key])#iterating through the dictionary and printing key-value pairs