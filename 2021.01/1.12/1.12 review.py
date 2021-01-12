# def factorial(n):
#     output = 1
#     for i in range(1, n + 1):
#         output *= i
#     return output

# print("5!",factorial(5))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print("5!",factorial(5))

# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print("피보나치", fibonacci(3))

# dictionary = {1 : 1, 2:2}

# def fibonacci(n):
#     if n in dictionary:
#         return dictionary[n]
#     else:
#         output = fibonacci(n-1) + fibonacci(n-2)
#         dictionary[n] = output
#         return output
# print(fibonacci(50))

def number_input():
    output = input("숫자입력")
    return output

def get_circumference(radius):
    return 2 * 3.14 * radius

def get_circle_area(radius):
    return 3.14 * radius * radius

radius = number_input()
print(get_circumference(radius))
print(get_circle_area(radius)) 