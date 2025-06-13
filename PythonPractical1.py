user_input = input("Enter numbers seperated by commas: ")
numbers = [int(num.strip()) for num in user_input.split(',')]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("The greatest number is:", max_num)
