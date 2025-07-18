def is_palindrome(text: str) -> bool:
    """
    Checks whether the given string is a palindrome.
    
    Parameters:
        text (str): The input string to be checked.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned string to its reverse
    return cleaned == cleaned[::-1]


def main():
    print("\n*** Palindrome Checker ***")
    user_input = input("Enter a string: ")

    if is_palindrome(user_input):
        print("Entered String is Palindrome!!")
    else:
        print("Entered String is not Palindrome!!")


if __name__ == "__main__":
    main()
