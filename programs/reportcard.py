name = input("Enter your name: ")
age = int( input("Enter your age: ") )
eng_marks = int( input("Enter your marks in English: ") )
math_marks = int( input("Enter your marks in Mathematics: ") )
science_marks = int( input("Enter your marks in Science: ") )

print("This is your report card")
print("******************************")
print("Name: " + name)
print("Age: " + str(age) )
print("Marks: ")
print("English | " + str(eng_marks))
print("Maths   | " + str(math_marks))
print("Science | " + str(science_marks))
print("----------------------------")
total_marks = eng_marks + math_marks + science_marks
if total_marks == 300:
    print("Total Marks = Full (Yay!)")
elif total_marks <= 100:
    print("Total Marks = Awww. Failed! Try again..")
else:
    print("Total Marks = " + str(total_marks) + "/300")
print("******************************")

