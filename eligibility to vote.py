# Write a script to accept name, age, and print eligibility to vote,
# Hint : Use input() print() int() methods, int() will be used for typecasting


def printname(myname):
    print("Hello"+" "+myname)


def printage(myage):
    print(myage)


if __name__ == '__main__':

  name=input("Enter Your Name:")
  print(type(name))
  printname(name)

  age=input("Enter Your Age:")
  age = int(age)
  print(type(age))
  printage(age)

  if age >= 18:
      print("You are eligible to vote.")
  else:
      print("You are not eligible to vote.")

