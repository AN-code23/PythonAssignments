# - Create a program to calculate perimeter of circle
# 	Hint : use int() for typecasting, converting str to int datatypes


def perimeter_circle(r_radius):
    perimeter=2 * 3.14 * r_radius
    print(perimeter)

if __name__ == '__main__':
    radius=int(input("Enter radius:"))
    print(type(radius))
    perimeter_circle(radius)