from typing import List

def is_valid_email(email: str) -> bool:
    """
    Checks if the provided email is valid.

    Args:
        email (str): The email to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))

def is_valid_password(password: str) -> bool:
    """
    Checks if the provided password is valid.

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def get_random_string(length: int) -> str:
    """
    Generates a random string of a specified length.

    Args:
        length (int): The length of the string to be generated.

    Returns:
        str: A random string of the specified length.
    """
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def get_random_int(min_value: int, max_value: int) -> int:
    """
    Generates a random integer within a specified range.

    Args:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.

    Returns:
        int: A random integer within the specified range.
    """
    import random
    return random.randint(min_value, max_value)

def get_current_user() -> dict:
    """
    Returns the current user's details.

    Returns:
        dict: A dictionary containing the current user's details.
    """
    # Replace this with your actual user retrieval logic
    return {
        'id': 1,
        'email': 'user@example.com',
        'name': 'John Doe'
    }

def get_current_request() -> dict:
    """
    Returns the current request's details.

    Returns:
        dict: A dictionary containing the current request's details.
    """
    # Replace this with your actual request retrieval logic
    return {
        'method': 'GET',
        'path': '/',
        'headers': {}
    }