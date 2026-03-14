import json

student = {
    "name": "John",
    "age": 21,
    "course": "Python"
}

# Write JSON file
with open("student.json", "w") as file:
    json.dump(student, file)

# Read JSON file
with open("student.json", "r") as file:
    data = json.load(file)

print("Data read from JSON file:")
print(data)
