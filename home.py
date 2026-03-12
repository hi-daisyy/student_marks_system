print("Welcome to Student Marks System")
print("Developed by daisy")

# This will run exactly 3 times
for i in range(3):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    print(name, "scored", marks)
    print("---------") # Just to separate the entries