# Switch / Match in Python
# Python uses match/case for switch-like behavior.
# Example 1: Match a day number.
day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")

# Example 2: Match a menu choice.
choice = "start"
match choice:
    case "start":
        print("Starting...")
    case "settings":
        print("Opening settings...")
    case "quit":
        print("Goodbye!")
    case _:
        print("Unknown choice")

# Example 3: Match several values with one case.
number = 3
match number:
    case 1 | 2 | 3:
        print("Number from 1 to 3")
    case _:
        print("Other number")

# Example 4: Match with a condition (guard).
score = 85
match score:
    case n if n >= 90:
        print("Excellent")
    case n if n >= 60:
        print("Passed")
    case _:
        print("Failed")

# Example 5: Match a simple tuple.
point = (0, 0)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print("On the x-axis")
    case (0, y):
        print("On the y-axis")
    case _:
        print("Somewhere else")
