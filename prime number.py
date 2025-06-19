#- Write a program to check if a number is prime, take number as input

n=int(input("Enter a number:"))
sq_num=n**0.5
if n <= 1:
    print("Not a prime number")

elif n == 2:
    print("Prime number")

elif n % 2==0:
    print("Not a prime number")

else:
    print("Prime number")