# .................................. Python Basics Programs....................................

# 1. Find Square root of a number
num= int(input("Enter a Number"))
sqrt= num**(1/2)
print("Square Root is", sqrt)

# 2. Python Program to Calculate the Area of a Triangle
a=int(input("Enter 1st length: "))
b=int(input("Enter 2nd length: "))
c=int(input("Enter 3rd length: "))
area= (a+b+c)/2;
print("Area is",area)


# 3. Python Program to Solve Quadratic Equation -b+ root(b**2-4ac)/2a
b=int(input("Enter a number"))
a=int(input("Enter 2nd no"))
c=int(input("Enter 3rd no"))
d=(-b+((b**2-(4*a*c))**0.5))/(2*a)
print(d)

# 4. Python Program to Swap Two Variables
a = int(input("Enter a number"))
b=int(input("Enter 2nd number"))
c=a
a=b
b=c
print(a)
print(b)

# 5. Python Program to Convert Kilometers to Miles
km = int(input("Enter in KMs"))
miles=km*0.621
print(miles,"miles")

# 6. Python Program to Convert Celsius To Fahrenheit
cel = int(input("Enter Temperature"))
far=(cel*1.8)+32
print(far,"Fahrenheit")

# 7. Python Program to Check if a Number is Positive, Negative or 0
a=int(input("Enter a number"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")
# 8. Python Program to Check if a Number is Odd or Even
num=int(input("Enter a number: "))
if num%2==0:
    print("It is a even number")
else:
    print("It is odd number")
# 9. Python Program to Check Leap Year
year=int(input("Enter Year: "))
if year%4==0:
    print("It is leap year")
else:
    print("It is not a leap year")

# 10. Python Program to Find the Largest Among Three Numbers
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
c=int(input("Enter 3rd Number"))
if a>b:
    print(a,"is greater")
elif b>c:
    print(b,"is greater")
elif c>a:
    print(c,"is greater")
else:
    print("Incorrect Number")

# 11. Python Program for simple interest
p=int(input("Enter Principal Amount: "))
t=int(input("Enter time duration: "))
r=int(input("Enter rate of interest: "))
i=(p*t*r)/100;
print("Interest is:",i)
print("Total is: ",p+i)

# 12. Area of Circle
r=int(input("Enter radius"))
area=3.14*r*r
print(area)

# 13. Check Vowel or Consonant using if-else
a=input("Enter an alphabet: ")
if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
    print("It is a vowel")
else:
    print("It is a consonant")

# 14. Average of three numbers
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))
avg=(a+b+c)/3
print("Average is: ",avg)

# 15. Find Area of Square
l=int(input("Enter Length"))
area=l**2
print(area)

# 16.0Find Area of Rectangle
l=int(input("Enter Length: "))
b=int(input("Enter breadth: "))
print("area is: ",l*b)

# 17. Find Area of Triangle based on Base and Height
b=int(input("Enter Base of Triangle: "))
h=int(input("Enter Height of Triangle: "))
area=(1/2)*b*h
print(area)

# 18. circumferrence of a circle
r=int(input("Enter Radius:"))
circ=2*3.14*r
print("The Circumferrence is:",circ)

# 19. Python program to find Cube of a Number
n=int(input("Enter a number"))
cube=n**3
print("Cube is: ",cube)

# 20. Python program to find square root of a Number
n=int(input("Enter a number"))
sqrt=n**0.5
print("Square root is: ",sqrt)

# 21. Python program to find Square of a Number
n=int(input("Enter a number"))
sq=n**2
print("Square is: ",sq)

# 22. Python program to check Number Divisible by 5 and 11
num=int(input("Enter a number: "))
if num%5==0:
    print("It is divisible by 5")
elif num%11==0:
    print("It is divisible by 11")
else:
    print("This is not divisible by 5 or 11")

# 23. Python program for Multiplication Table
num=int(input("Enter a number: "))
print("Multiplication Table is:")
print(num*1)
print(num*2)
print(num*3)
print(num*4)
print(num*5)
print(num*6)
print(num*7)
print(num*8)
print(num*9)
print(num*10)

# 24. Python Program to Find Numbers Divisible by Another Number
num=int(input("Enter the number you want to divide: "))
div=int(input("Enter the divisor: "))
if num%div==0:
    print("It is divisible")
else:
    print("Not divisible")

'''
Python Program to Check Prime Number
Python program for Arithmetic Operations
Python program to print Calendar
Python program to Print Natural number 1 to N
Python program for Leap Year
Python program to find Odd or Even
Python program to print Even Numbers from 1 to 100
Python program to print Odd Numbers from 1 to 100
Python Program to Print Negative Numbers in a Range
Python Program to Print Positive Numbers in a Range
Python program to find Positive or Negative
Python program to find Profit Or Loss
Python program to find Square of a Number
Python program to find Square root of a Number
Python Program to find all divisors of an integer
Python Program to find Compound Interest
Python program to check Number Divisible by 5 and 11
Python program to find Power of a Number
Python program for Multiplication Table
Python example to find Roots of a Quadratic Equation
Python example to find Student Grade
Python example to find Simple Interest
Python Program to Read 10 Numbers and Find their Sum and Average
Python Program to Print First 10 Even Natural Numbers
Python Program to Print First 10 Natural Numbers
Python Program to Print First 10 Natural Numbers in Reverse
Python Program to Print First 10 Odd Natural Numbers
Python program to Print Natural number 1 to N
Python program to print Natural Numbers in Reverse Order
Python example to find Sum and Average of Natural Numbers
Python Program to Find Sum of 10 Numbers and Skip Negative Numbers
Python Program to Find Sum of 10 Numbers until user enters Positive Numbers
Python example to Calculate Electricity Bill
Python Program to Find Distance Between Two Points
Python Program to Get Current Date and Time
Python Program to Make a Simple Calculator
# Python Program to Generate a Random Number
# Python Program to Print all Prime Numbers in an Interval
# Python Program to Find the Factorial of a Number
# Python Program to Display the multiplication Table
# Python Program to Print the Fibonacci sequence
# Python Program to Check Armstrong Number
# Python Program to Find Armstrong Number in an Interval
# Python Program to Find the Sum of Natural Numbers
# Python Program to Display Powers of 2 Using Anonymous Function
# Python Program to Find Numbers Divisible by Another Number
# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
# Python Program to Find ASCII Value of Character
# Python Program to Find HCF or GCD
# Python Program to Find LCM
# Python Program to Find the Factors of a Number
# Python Program to Make a Simple Calculator
# Python Program to Shuffle Deck of Cards
'''
