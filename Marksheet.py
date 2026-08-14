#Marksheet for Students

print("Please Enter the marks as whole number!")
Math=int(input("Enter the marks in Maths:"))
Eng=int(input("Enter the marks in English:"))
Hind=int(input("Enter the marks in Hindi:"))
Sci=int(input("Enter the marks in Science:"))
Sco_Sci=int(input("Enter the marks in Social Science:"))

Total=Math+Eng+Hind+Sci+Sco_Sci
Avg=(float(Total/5))

print("Total= ",Total)
print("Avg= ",Avg)