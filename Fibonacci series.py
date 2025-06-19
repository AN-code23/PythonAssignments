#- Generate the Fibonacci series up to n terms, take n as input from user

n = int(input("Enter number: "))

a=0
b=1

print(a, b, end=" ")

for i in range(n - 2):
    res = a + b
    print(res, end=" ")
    a = b
    b = res
