english_marks = int(input("enter student marks in English: "))
math_marks = int(input("enter student marks in Maths: "))

overall_grade = ""
english_grade = ""

if (english_marks > 80) and (math_marks > 90):
	overall_grade = "A+"
	english_grade = "A+"
elif (english_marks > 80) and (math_marks >= 80):
	overall_grade = "A"
	english_grade = "A+"
elif (english_marks > 50) and (math_marks >= 80):
	overall_grade = "A"
	english_grade = "B"
else:
	overall_grade = "B"
	english_grade = "B"


print("Overall grade: {} English grade: {}".format(overall_grade, english_grade))
	
