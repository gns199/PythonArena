name = input("Enter Student Name: ")
print("Enter Student Marks in....")
od = int(input("Odia: "))
eng = int(input("English: "))
mth = int(input("Mathematics: "))
sc = int(input("Science: "))
his = int(input("History: "))
marks = od + eng + mth + sc + his
print("Total Marks Allotted:", marks)
perc = marks / 5
print("In Percentage: ", perc)
if perc >= 90:
    print("Grade A")
elif perc >= 70:
    print("Grade B")
elif perc >= 50:
    print("Grade C")
elif perc >= 30:
    print("Grade D")
else:
    print("Grade F")
