#write a program to greet user:
#Take name, age interests as input from user and print it in console:
#Bank balance, if interested in our course:



def greetuser(my_name):
    print('Hello'+" "+ my_name)

# def printmyname(my_name):
#     print (my_name)

def printmyage(my_age):
    print(my_age)

def printmyinterests(my_interests):
    print(my_interests)

def printmybank(my_bank):
    print(my_bank)


#def printare_you_interested(are_you_interested):
   # printare_you_interested(are_you_interested)


if __name__ == '__main__':
     name=input("enter your name:")
     greetuser(name)
    # print("Atish here")
     #print("Welcome to the class")

     # name=input("Enter Your Name:")
     # printmyname(name)

     age=input("Enter Your Age:")
     age = int(age)
     print(type(age))
     printmyage(age)

     interests=input("Enter Your Interests:")
     print(type(interests))
     printmyinterests(interests)

     Bank=input("Enter Your Bank Balance:")
     Bank = float(Bank)
     print(type(Bank))
     printmybank(Bank)

     are_you_interested=input("Are you interested ?")
     print("Your response is" + are_you_interested)

     are_you_interested = input("Are you interested ?")
     are_you_interested = bool(are_you_interested)
     print(type(are_you_interested))