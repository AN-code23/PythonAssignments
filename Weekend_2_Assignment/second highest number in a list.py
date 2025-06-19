# Write a program to find the second highest number in a list

numbers=[10,56,28,3,6,99,2,2]

numbers=list(set(numbers))
numbers.sort(reverse=True)


print("Second highest number is:",numbers[1])

# second highest from the end

numbers = [10, 56, 28, 3, 6, 99, 2, 2]

numbers = list(set(numbers))
numbers.sort(reverse=True)


print("Second highest number is:",numbers[-2])


