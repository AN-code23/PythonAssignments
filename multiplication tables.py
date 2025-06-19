# - Print multiplication tables from 1 to 10 using loops

n= int(input("Enter a number:"))
for i in range(1,11):
    print(n, "*", i,"=",n*i)