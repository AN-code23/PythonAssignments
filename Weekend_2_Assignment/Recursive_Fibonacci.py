def fi(num):
    if num<=1:
        return num
    return fi(num-1) + fi(num-2)


def fact(num):
    if num==0 or num==1:
        return 1
    return num* fact(num-1)


if __name__ == '__main__':
    n = int(input("Enter number: "))

    for i in range(n):
        # f=fi(i)
        print("Factorial of ",i ,"is:",fact(i))




















