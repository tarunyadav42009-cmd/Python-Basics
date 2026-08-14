# Marksheet for Students
print("Please Enter the marks as whole number!")

# Input marks for 5 subjects
Math = int(input("Enter the marks in Maths: "))
Eng = int(input("Enter the marks in English: "))
Hind = int(input("Enter the marks in Hindi: "))
Sci = int(input("Enter the marks in Science: "))
Sco_Sci = int(input("Enter the marks in Social Science: "))

# Calculations
Total = Math + Eng + Hind + Sci + Sco_Sci
Avg = Total / 5  # Python 3 automatically converts division to float

# Output results
print("\nTotal =", Total)
print("Avg =", Avg)
if(Math<35 or Hind<35 or Sci<35 or Sco_Sci<35 or Eng<35):
    print("Remark: Fail!")
else:
    print("Remark: Pass!")

# Grading Logic
if Avg < 33:
    print("Grade: Fail!")
elif 33 <= Avg <= 60:  
    print("Grade: Pass!")
elif 60 < Avg <= 75:
    print("Grade: First Class!")
else:  # Handles everything above 75
    print("Grade: First Class with Distinction!")


