# Q1 Sum of two numbers
a, b = 10, 5
print(a + b)

# Q2 Difference
print(a - b)

# Q3 Product
print(a * b)

# Q4 Quotient
print(a / b)

# Q5 Remainder
print(a % b)

# Q6 Swap using third variable
a, b = 10, 20
temp = a
a = b
b = temp
print(a, b)

# Q7 Swap without third variable
a, b = 10, 20
a, b = b, a
print(a, b)

# Q8 Last digit of N
a = int(input("Enter a number: "))
print(a % 10)

# Q9 All digits except last
print(N // 10)

# Q10 Sum of first and last digit of 3-digit number
N = 123
first = N // 100
last = N % 10
print(first + last)

# Q11 Middle digit of 3-digit number
print((N // 10) % 10)

# Q12 Absolute value
num = -42
print(abs(num))

# Q13 Square
num = 5
print(num ** 2)

# Q14 Cube
print(num ** 3)

# Q15 Average of three numbers
a, b, c = 10, 20, 30
print((a + b + c) / 3)

# Q16 Check for eauality of two numbers
a , b = map(int, input("Enter two numbers: ").split())
if( a == b ):
    print("TRUE")
else:
    print("FALSE")
    
#Q17 check for square of a number using AND operator
num = int(input("Enter the number with power:"))
if(num > 0 and num ** 2 > 0):
    print("The square of the number is: ", num ** 2)

#Q18 check for positive number or negative number
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
    
#Q19 Greatest of three numbers
a, b, c = map(int, input("Enter three numbers: ").split())
if a >= b and a >= c:
    print("Greatest number is:", a)
elif b >= a and b >= c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)
    
    
#Q20 Pass or fail based on marks
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")
    