import pandas as pd

# Creating student data
students = {
    "Name": ["Kiran", "Rahul", "Priya", "Sneha", "Arjun"],
    "Age": [23, 22, 21, 24, 22],
    "Marks": [85, 65, 92, 48, 78],
    "Department": ["MCA", "BCA", "MCA", "BBA", "MCA"]
}

df = pd.DataFrame(students)

print("Student Dataset:")
print(df)

# Filter students who scored more than 80
print("\nStudents who scored above 80:")
result1 = df[df["Marks"] > 80]
print(result1)

# Filter students from MCA department
print("\nStudents from MCA department:")
result2 = df[df["Department"] == "MCA"]
print(result2)

# Filter students who scored above 75 and are older than 21
print("\nStudents with marks above 75 and age above 21:")
result3 = df[(df["Marks"] > 75) & (df["Age"] > 21)]
print(result3)

# Display the number of records
print("\nTotal students scoring above 80:", len(result1))
print("Total MCA students:", len(result2))
print("Total students matching both conditions:", len(result3))
