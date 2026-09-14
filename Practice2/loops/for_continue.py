# For Loop Continue
# Example 1: Skip number 3.
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# Example 2: Print only even numbers.
for number in range(1, 11):
    if number % 2 != 0:
        continue
    print(number)

# Example 3: Skip a word.
fruits = ["apple", "skip", "banana", "cherry"]
for fruit in fruits:
    if fruit == "skip":
        continue
    print(fruit)

# Example 4: Skip negative values.
numbers = [5, -2, 8, -1, 3]
for number in numbers:
    if number < 0:
        continue
    print(number)

# Example 5: Skip vowels.
for letter in "PYTHON":
    if letter in "AEIOU":
        continue
    print(letter)
