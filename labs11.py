# lab_11-8.py

def length_multiples(input_list):
    new_list = [item * index for index, item in enumerate(input_list)]
    return new_list

# Test cases

test_list1 = [1, 2, 3, 4, 5]
result1 = length_multiples(test_list1)
print("Test case 1 result:", result1)

test_list2 = [1.0, 2, 3.5, 4, 5.2]
result2 = length_multiples(test_list2)
print("Test case 2 result:", result2)

test_list3 = ["a", "b", "c", "d"]
result3 = length_multiples(test_list3)
print("Test case 3 result:", result3)

# lab_11-2.py

def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()
    return cleaned_string == cleaned_string[::-1]

# Test cases
print(is_palindrome("racecar")) 
print(is_palindrome("A man a plan a canal Panama")) 
print(is_palindrome("hello world")) 

# lab_11-3.py

import random

def number_guess():
    secret_number = random.randint(1, 100)
    
    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 100: "))
            
            if user_guess == secret_number:
                print("Congratulations! You guessed the correct number.")
                break
            elif user_guess < secret_number:
                print("Not correct. The number is higher.")
            else:
                print("Not correct. The number is lower.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 100.")

number_guess()
# lab_11-4.py

def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer greater than 1."
    elif n == 1:
        return "Fibonacci sequence with 1 value: [0]"
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)

        print(f"Fibonacci sequence with {n} values: {fib_sequence}")
        return sum(fib_sequence)

try:
    user_input = int(input("Enter the number of Fibonacci values to generate (2-100): "))
    result = fibonacci(user_input)
    print(f"Sum of the Fibonacci sequence: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer between 2 and 100.")
  

# lab_11-5.py

def name_multiplication(names):
    for name in names:
        for _ in range(len(name)):
            print(name)

names_list = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names_list.append(name)

name_multiplication(names_list)

# lab_11-6.py

total_sum = 0

while True:
    try:
        user_input = float(input("Enter a number (or -1 to quit): "))
        
        if user_input == -1:
            break
        
        total_sum += user_input
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"Sum of all numbers entered: {total_sum}")

