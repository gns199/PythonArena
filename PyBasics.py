# .................................. Python Basics Programs....................................

# Find Square root of a number
num= int(input("Enter a Number"))
sqrt= num**(1/2)
print("Square Root is", sqrt)

# Python Program to Calculate the Area of a Triangle
a=int(input("Enter 1st length: "))
b=int(input("Enter 2nd length: "))
c=int(input("Enter 3rd length: "))
area= (a+b+c)/2;
print("Area is",area)


# Python Program to Solve Quadratic Equation -b+ root(b**2-4ac)/2a
b=int(input("Enter a number"))
a=int(input("Enter 2nd no"))
c=int(input("Enter 3rd no"))
d=(-b+((b**2-(4*a*c))**0.5))/(2*a)
print(d)

# Python Program to Swap Two Variables
a = int(input("Enter a number"))
b=int(input("Enter 2nd number"))
c=a
a=b
b=c
print(a)
print(b)

# Python Program to Convert Kilometers to Miles
km = int(input("Enter in KMs"))
miles=km*0.621
print(miles,"miles")

# Python Program to Convert Celsius To Fahrenheit
cel = int(input("Enter Temperature"))
far=(cel*1.8)+32
print(far,"Fahrenheit")

# Python Program to Check if a Number is Positive, Negative or 0
a=int(input("Enter a number"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")
# Python Program to Check if a Number is Odd or Even
num=int(input("Enter a number: "))
if num%2==0:
    print("It is a even number")
else:
    print("It is odd number")
# Python Program to Check Leap Year
year=int(input("Enter Year: "))
if year%4==0:
    print("It is leap year")
else:
    print("It is not a leap year")

# Python Program to Find the Largest Among Three Numbers
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
# Python Program for simple interest
p=int(input("Enter Principal Amount: "))
t=int(input("Enter time duration: "))
r=int(input("Enter rate of interest: "))
i=(p*t*r)/100;
print("Interest is:",i)
print("Total is: ",p+i)

#Area of Circle
r=int(input("Enter radius"))
area=3.14*r*r
print(area)

#Check Vowel or Consonant using if-else
a=input("Enter an alphabet: ")
if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
    print("It is a vowel")
else:
    print("It is a consonant")
#Average of three numbers
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))
avg=(a+b+c)/3
print("Average is: ",avg)
#Find Area of Square
l=int(input("Enter Length"))
area=l**2
print(area)

#Find Area of Rectangle
l=int(input("Enter Length: "))
b=int(input("Enter breadth: "))
print("area is: ",l*b)

#Find Area of Triangle based on Base and Height
b=int(input("Enter Base of Triangle: "))
h=int(input("Enter Height of Triangle: "))
area=(1/2)*b*h
print(area)

#circumferrence of a circle
r=int(input("Enter Radius:"))
circ=2*3.14*r
print("The Circumferrence is:",circ)

# Python Program to Check Prime Number

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

