student = {
    "name": "John Doe",
    "age": 20,
    "course_name": "Algebra",
    "grade": 70.89,
}

print(student)

student["email"] = "test@gmail.com"
student["name"] = "Solomon"

# del student["grade"]
student.pop("grade")
print(student)