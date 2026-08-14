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

if(Avg<33):
    print("Fail!")

elif(Avg>33 and Avg<=60):
    print("Pass!")

elif(Avg>60 and Avg<=75):
    print("First Class!")
    
elif(Avg>75):
    print("First Class with Distinction!")    


