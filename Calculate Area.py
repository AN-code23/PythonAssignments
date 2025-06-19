#Create a program to calculate area of rectangle, circle, and triangle


def area_rectangle(length_l,width_w):
    area=length_l*width_w
    print(area)


def area_circle(r_radius):
    area=3.14 * r_radius * r_radius
    print(area)


def area_triangle(b_base, h_height):
    area=0.5*b_base*h_height
    print(area)


if __name__ == '__main__':
    length=float(input("enter length:"))
    width = float(input("enter width:"))
    area_rectangle(length,width)

    radius=float(input("Enter radius:"))
    area_circle(radius)

    base=float(input("Enter base:"))
    height=float(input("Enter height:"))
    area_triangle(base,height)


# base=int(input("enter base:"))
# height= int(input("enter height:"))
# area=0.5*base*height
# print(area)