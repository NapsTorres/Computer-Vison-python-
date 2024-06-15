# 7.1
def count(string):
    upper = 0
    lower = 0
    length = len(string)
    total = 0
    
    while total < length:
        char = string[total]
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        total += 1
    
    return upper, lower

User_Input = input("Enter a String: ")
upper, lower = count(User_Input)
print("No. of uppercase letters:", upper)
print("No. of lowercase letters:", lower)

# 7.2
Given_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Num = 0
even_numbers = []

while True:
    if Given_numbers[Num] % 2 == 0:
        even_numbers.append(Given_numbers[Num])
    Num += 1
    if Num >= len(Given_numbers):
        break

print("Even numbers:", even_numbers)


# 7.3
while True:
    input_rows = int(input("Enter a Number: "))
    if input_rows > 0:
        break

def pascal(n, triangle=None, i=0):
    if triangle is None:
        triangle = []
    if i == n:
        return triangle
    if i == 0:
        triangle.append([1])
    else:
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)
    return pascal(n, triangle, i + 1)

pascals_triangle = pascal(input_rows)
for row in pascals_triangle:
    print(row)







