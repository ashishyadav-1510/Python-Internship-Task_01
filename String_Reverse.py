def reverse_string(input_string):
    """
    Reverses the given string using slicing.
    Parameters:
        input_string (str): The string to be reversed.
    Returns:
        str: The reversed version of the input string.
    """
    return input_string[::-1]

def main():
    print("String Reversal Program")
    user_input = input("Enter a string to reverse: ").strip()

    if not user_input:
        print("Empty input provided. Please enter a valid string.")
        return

    reversed_result = reverse_string(user_input)
    print("\nReversed String:")
    print(reversed_result)

if __name__ == "__main__":
    main()
