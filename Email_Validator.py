import re

def is_valid_email(email: str) -> bool:
    """
    Validates whether the given string is a properly formatted email address.

    Parameters:
        email (str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def main():
    print("Email Validator Checker")
    email_input = input("Enter an email address to validate: ").strip()

    if not email_input:
        print("Email address cannot be empty.")
        return

    if is_valid_email(email_input):
        print(f"'{email_input}' is a valid email address.")
    else:
        print(f"'{email_input}' is NOT a valid email address.")

if __name__ == "__main__":
    main()
