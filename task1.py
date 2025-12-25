# 1 .Sum of Two Numbers

a=int(input("Enter the 1st value:"))
b=int(input("Enter the 2nd value"))
sum=a+b
print("sum:",sum)

# 2.Odd or Even Checker

n=int(input("Enter the num:"))
if(n%2==0):
    print("Even Number")
else:
    print("Odd number")

# 3.Factorial calculation

def factorial(n):
    if(n==0):
        return 1
    else:
        return n *factorial (n-1)
num=int(input("enter the num:"))
print("Factorial is:",factorial(num))

# 4.Fibonacci Sequence

num=int(input("Enter the num:"))
a,b=0,1
for i in range(num):
    print(a,end='')
    a,b=b,a+b
    
# 5.Reverse string

word=input("Enter the word:")
print(word[::-1])

# 6.palindrome Check

word=input("Enter the word:")
if(word==word[::-1]):
    print("palindrome")
else:
    print("not palindrome")

# 7.Leap year check

y=int(input("Enter the year:"))
if(y%4==0):
    print("Leap year")
else:
    print("not a leap year")


# 8.Amstrong Number

num=int(int(input("Enter the num:")))
temp=num
digits=len(str(num))
sum=0
while temp> 0:
    digit =temp%10
    sum +=digit **digits
    temp=temp//10
if(sum==num):
    print("amstrong")
else:
    print("not an amstrong")    




                                         
