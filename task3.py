"""
Write a function calculate_grade(score) that takes a student’s numeric score (an integer between 0 and 100) and returns their letter grade based on the following rules:
90–100 → A
80–89 → B
70–79 → C
60–69 → D
Below 60 → F
Make sure your function works for all boundary values (e.g., 60, 70, 80, 90, 100).

Expected output
print(calculate_grade(95))   # A
print(calculate_grade(88))   # B
print(calculate_grade(72))   # C
print(calculate_grade(65))   # D
print(calculate_grade(40))   # F
print(calculate_grade(100))  # A
print(calculate_grade(60))   # D
print(calculate_grade(70))   # C
print(calculate_grade(89))   # B
"""


score = float(input("Enter Score: "))

def calculate_grade(score):
	if score <=100 and score >=90:
		print("A")
	elif score >=80 and score <90:
		print("B")
	elif score >=70 and score <80:
		print("C")
	elif score >=  60 and score <70:
		print("D")
	elif score <60:
		print("F")
	else:
		print("Invalid Score:")


calculate_grade(score)
