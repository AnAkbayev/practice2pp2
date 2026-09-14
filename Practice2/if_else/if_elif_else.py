# If Elif Else
# Example 1: Choose a message based on age.
age = 25
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# Example 2: Grade classification.
score = 82
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")

# Example 3: Temperature description.
temperature = 15
if temperature > 25:
    print("Hot")
elif temperature >= 10:
    print("Comfortable")
else:
    print("Cold")

# Example 4: Compare a number with zero.
number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Example 5: Simple traffic-light decision.
light = "yellow"
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
else:
    print("Go")
