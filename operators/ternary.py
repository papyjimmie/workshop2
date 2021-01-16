# EX1

number1, number2 = 10, 20

min = number1 if number1 < number2 else number2

print(min)

# Output: 10

# EX2

# Python program to demonstrate nested ternary operator
a, b = 10, 20

print(
    "Both a and b are equal"
    if a == b
    else "a is greater than b"
    if a > b
    else "b is greater than a"
)

# # Python program to demonstrate nested ternary operator

# if a != b:
#     if a > b:
#         print("a is greater than b")
#     else:
#         print("b is greater than a")
# else:
#     print("Both a and b are equal")
