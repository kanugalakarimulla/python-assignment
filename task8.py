
# Q8. Write a function that handles the ValueError exception that may be raised when trying to
# convert a string to an integer. The function should prompt the user to enter a new string until
# a valid integer is entered.

# Input: '3'
# Output: 3

# Input: 'abc'
# Output: ValueError exception handled, new input prompted.

def check_integer():
    user_value = input("Enter an integer: ")
    try:
        return int(user_value)
    except ValueError:
        print(f"{user_value} is not a valid integer. Please try again.")
        return check_integer()


print(check_integer())
