def get_integer_input() -> int:
    """
    Prompt the user to enter a valid integer.

    Returns:
        int: The validated integer input by the user.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


def check_even_odd(number: int) -> str:
    """
    Determine whether a given number is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: A message indicating if the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."


if __name__ == "__main__":
    # Get user input and display the result
    user_number = get_integer_input()
    result = check_even_odd(user_number)
    print(result)
def get_integer_input():

    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):

    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."


number = get_integer_input()
result = check_even_odd(number)
print(result)
