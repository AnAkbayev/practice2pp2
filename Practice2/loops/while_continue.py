# While Loop Continue
# Example 1: Skip the number 3.
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# Example 2: Print only odd numbers.
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)

# Example 3: Skip a specific word.
words = ["apple", "skip", "banana", "cherry"]
i = 0
while i < len(words):
    word = words[i]
    i += 1
    if word == "skip":
        continue
    print(word)

# Example 4: Skip negative numbers.
numbers = [5, -2, 8, -1, 3]
i = 0
while i < len(numbers):
    value = numbers[i]
    i += 1
    if value < 0:
        continue
    print(value)

# Example 5: Continue until the counter reaches 5.
count = 0
while count < 5:
    count += 1
    if count == 4:
        continue
    print("Count:", count)
