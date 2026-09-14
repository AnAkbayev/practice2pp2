# While Loop Break
# Example 1: Stop when the counter reaches 3.
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

# Example 2: Break when a number is found.
number = 1
while number <= 10:
    if number == 7:
        break
    print(number)
    number += 1

# Example 3: Stop a countdown early.
count = 5
while count > 0:
    print(count)
    if count == 2:
        break
    count -= 1

# Example 4: Search for a value.
numbers = [2, 4, 6, 8, 10]
index = 0
while index < len(numbers):
    if numbers[index] == 6:
        print("Found 6")
        break
    index += 1

# Example 5: Break from an input-style loop.
attempts = 0
while attempts < 5:
    attempts += 1
    print("Attempt", attempts)
    if attempts == 3:
        break
