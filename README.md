# TASK - 1 : String Reversal

A simple Python program that reverses a given string using slicing.

### Features

* Takes a string as input from the user.
* Returns the reversed string.
* Validates against empty input.
* Clean and modular code with a `main()` function.

### How It Works

1. The program defines a function `reverse_string()` that reverses the string using slicing (`[::-1]`).
2. It then prompts the user for input.
3. If the input is valid (not empty), it displays the reversed result.

### Usage
Run the script using Python:
python String_Reverse.py

Example Output:
String Reversal Program
Enter a string to reverse: hello

Reversed String:
olleh

## Screenshot
### Code:
![image](https://github.com/ashishyadav-1510/Python-Internship-Task_01/blob/main/Screenshot/Task1/Screenshot%202025-07-18%20135911.png?raw=true)
### Output:
![image](https://github.com/ashishyadav-1510/Python-Internship-Task_01/blob/main/Screenshot/Task1/Screenshot%202025-07-18%20135929.png?raw=true)

## Video

[Video]()


## Explanation
def reverse_string(input_string):
Defines a function named reverse_string which takes one argument input_string (a string).

    """
    Reverses the given string using slicing.
    Parameters:
        input_string (str): The string to be reversed.
    Returns:
        str: The reversed version of the input string.
    """
Multiline docstring that explains what the function does, what parameter it takes, and what it returns.

    return input_string[::-1]
Returns the reversed string using Python slicing.

[::-1] is a slicing technique that means:
Start from the end of the string.
Go to the beginning.
Step -1 (i.e., in reverse).

def main():
Defines the main() function — this is the entry point of the program.

    print("String Reversal Program")
Displays a welcome message to the user.

    user_input = input("Enter a string to reverse: ").strip()
Prompts the user to enter a string.

.strip() removes any leading/trailing whitespace (spaces, newlines, etc.).

    if not user_input:
Checks if the user provided an empty string (e.g., just pressed Enter).

        print("Empty input provided. Please enter a valid string.")
If the string is empty, informs the user.

        return
Exits the main() function without doing anything further.

    reversed_result = reverse_string(user_input)
Calls the reverse_string() function with the user’s input and stores the result in reversed_result.

    print("\nReversed String:")
Prints a heading for the reversed string output.

    print(reversed_result)
Prints the reversed string.

if __name__ == "__main__":
This ensures that main() is only called when the script is run directly, not when it’s imported as a module.

    main()
Calls the main() function to execute the program.


# TASK - 2 : Temperature Conversion Program

A simple and interactive Python program to convert temperatures between **Celsius**, **Fahrenheit**, and **Kelvin**. This beginner-friendly project demonstrates conditional logic, functions, and user input validation in Python.

## Features

- Converts temperature values between **Celsius**, **Fahrenheit**, and **Kelvin**
- Accepts user input with input validation for both temperature and unit
- Supports case-insensitive unit input like `celsius`, `C`, `fahrenheit`, `F`, etc.
- Displays neatly formatted output with rounded values
- Beginner-friendly code and modular structure using functions

## How It Works

### 1. Input from User

The program asks the user to input:

- A temperature value (must be a valid number)
- The unit of the temperature (`celsius`, `fahrenheit`, `kelvin` or their short forms: `c`, `f`, `k`)

Invalid inputs trigger re-prompts until the correct format is entered.

### 2. Conversion Logic

Based on the entered unit, the program uses corresponding formulas:

| From → To            | Formula                       |
| --------------------- | ----------------------------- |
| Celsius → Fahrenheit | (°C × 9/5) + 32             |
| Celsius → Kelvin     | °C + 273.15                  |
| Fahrenheit → Celsius | (°F − 32) × 5/9            |
| Fahrenheit → Kelvin  | ((°F − 32) × 5/9) + 273.15 |
| Kelvin → Celsius     | K − 273.15                   |
| Kelvin → Fahrenheit  | ((K − 273.15) × 9/5) + 32   |

## Code Overview

### Conversion Functions

```python
def celsius_to_fahrenheit(c): return ((c * 9/5) + 32)
def celsius_to_kelvin(c): return (c + 273.15)
def fahrenheit_to_celsius(f): return ((f - 32) * 5/9)
def fahrenheit_to_kelvin(f): return (((f - 32) * 5/9) + 273.15)
def kelvin_to_celsius(k): return (k - 273.15)
def kelvin_to_fahrenheit(k): return (((k - 273.15) * 9/5) + 32)
```

## ScreenShots
## Code:
![image](https://github.com/ashishyadav-1510/Python-Internship-Task_01/blob/main/Screenshot/Task2/Screenshot%202025-07-18%20140004.png?raw=true)
## Output:
![image](https://github.com/ashishyadav-1510/Python-Internship-Task_01/blob/main/Screenshot/Task2/Screenshot%202025-07-18%20140042.png?raw=true)

## Video:
[Video on YouTube]()


### Explaination

1. **Temperature Conversion Functions**
   These are basic mathematical functions that convert temperature from one unit to another.

def celsius_to_fahrenheit(c):
    return ((c * 9/5) + 32)
Converts Celsius to Fahrenheit

Formula: (°C × 9/5) + 32 = °F

def celsius_to_kelvin(c):
    return (c + 273.15)
Converts Celsius to Kelvin

Formula: °C + 273.15 = K

def fahrenheit_to_celsius(f):
    return ((f - 32) * 5/9)
Converts Fahrenheit to Celsius

Formula: (°F − 32) × 5/9 = °C

def fahrenheit_to_kelvin(f):
    return (((f - 32) * 5/9)+ 273.15)
Converts Fahrenheit to Kelvin

Formula: (°F − 32) × 5/9 + 273.15 = K

def kelvin_to_celsius(k):
    return (k - 273.15)
Converts Kelvin to Celsius

Formula: K − 273.15 = °C

def kelvin_to_fahrenheit(k):
    return (((k - 273.15) * 9/5) + 32)
Converts Kelvin to Fahrenheit

Formula: (K − 273.15) × 9/5 + 32 = °F

2. **Main Conversion Logic**

def convert_temperature(value, unit):
    unit = unit.lower()
This function takes a numeric value and its unit (C, F, or K).

It converts the unit to lowercase for consistency ("C" becomes "c").

If input is Celsius:

    if(unit == "celsius" or unit == "c"):
        print(f"Entered Temperature: {value}°C")
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"Converted Temperature in other units: {round(f,2)}°F = {round(k,2)}K")
Calls the conversion functions to convert Celsius to Fahrenheit and Kelvin.

Displays the result using round() to format to 2 decimal places.

If input is Fahrenheit:

    elif(unit == "fahrenheit" or unit == "f"):
        print(f"Entered Temperature: {value}°F")
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"Converted Temperature in other units: {round(c,2)}°C = {round(k,2)}K")
Converts Fahrenheit to Celsius and Kelvin.

If input is Kelvin:

    elif(unit == "kelvin" or unit == "k"):
        print(f"Entered Temperature: {value}K")
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"Converted Temperature in other units: {round(c,2)}°C = {round(f,2)}°F")
Converts Kelvin to Celsius and Fahrenheit.

Invalid Unit:

    else:
        print("Invalid unit! Should not happen if input is validated.")
Fallback in case an invalid unit somehow reaches here.

3. **Program Starts Here**

print("*** Temperature Conversion Program ***")
Display welcome message

4. **User Input: Temperature Value**

while True:
    try:
        temp = float(input("Enter Value of Temperature = "))
        break
    except ValueError:
        print("!!Invalid Temperature!!\nPlease enter a valid Temperature(hint: numeric or float)")
Repeatedly prompts the user for a numeric temperature value.

Uses try-except to handle invalid inputs (non-numeric strings).

5. **User Input: Temperature Unit**

while True:
    unit = input("Enter Unit of Temperature (celsius,fahrenheit,kelvin)= ").lower()
    if(unit in ["celsius","c","fahrenheit","f","kelvin","k"]):
        break
    else:
        print("!!Wrong Unit!!\nPlease enter a valid Unit of Temperature (hint: Celcius, Fahrenheit, Kelvin)")
Asks for the unit of the input temperature.

Accepts multiple variations like "c" or "celsius", etc.

Keeps prompting until a valid unit is entered.

6. **Final Call to Conversion Function**

convert_temperature(temp, unit)
Once the temperature and its unit are successfully captured, it calls the main logic to do the conversion and print results.

Sample Output

*** Temperature Conversion Program ***
Enter Value of Temperature = 100
Enter Unit of Temperature (celsius,fahrenheit,kelvin)= celsius
Entered Temperature: 100.0°C
Converted Temperature in other units: 212.0°F = 373.15K


# Task - 3 : Email Validator
This Python script validates whether a given string is a properly formatted email address.

## Features
- Checks for valid email structure (e.g., user@example.com)
- Uses regular expressions to validate:
  - Presence of `@` symbol
  - Domain name (e.g., `.com`, `.org`)
  - Alphanumeric username

## How It Works
The `is_valid_email` function uses a regular expression pattern to match a valid email format:
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

### Example Valid Emails:
user123@example.com
my.email@domain.co.in

### Invalid Emails:
user@.com
@example.com
userexample.com

Usage
Run the script:

python email_validator.py
Enter an email address when prompted.
The program will validate and print whether the email is valid or not.

## ScreenShots
## Code:
![image](https://github.com/ashishyadav-1510/Python-Internship-Task_01/blob/main/Screenshot/Task3/Screenshot%202025-07-18%20140522.png?raw=true)
## Output:
![image](https://github.com/ashishyadav-1510/Python-Internship-Task_01/blob/main/Screenshot/Task3/Screenshot%202025-07-18%20140551.png?raw=true)

## Video:
[Video on YouTube]()

### Explaination

Importing Required Module

import re
re is Python’s regular expression module.
It allows you to search, match, and manipulate strings using patterns.

Email Validation Function

def is_valid_email(email: str) -> bool:
Defines a function named is_valid_email.
It takes one argument email (expected to be a string).
The function returns a bool (either True or False).

Docstring
    """
    Validates whether the given string is a properly formatted email address.

    Parameters:
        email (str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
Describes what the function does.
Includes documentation for the input (email) and output (True/False).

Regex Pattern
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
This line defines a regular expression (regex) pattern to match a valid email.
Breakdown of the pattern:
^: Start of string
[a-zA-Z0-9._%+-]+: Username part (alphanumeric and special characters allowed)
@: Must have a literal "@" symbol
[a-zA-Z0-9.-]+: Domain name (e.g., gmail, yahoo)
\.: A literal dot before domain extension
[a-zA-Z]{2,}: Top-level domain (e.g., com, org, in) with at least 2 characters
$: End of string

Checking Match
    return re.match(email_regex, email) is not None
Uses re.match() to check if the email fits the pattern.
Returns True if it matches, otherwise False.

Main Function
def main():
Entry point of the program. Runs the validation process.

Welcome Message
    print("Email Validator Checker")
Prints a heading to the user.

Get User Input
    email_input = input("Enter an email address to validate: ").strip()
Prompts user to enter an email.
.strip() removes any extra spaces from the beginning or end.

Empty Check
    if not email_input:
        print("Email address cannot be empty.")
        return
If the input is empty (""), display a warning and exit the function early using return.

Call Validator
    if is_valid_email(email_input):
        print(f"'{email_input}' is a valid email address.")
Calls the is_valid_email() function.
If it returns True, print confirmation that the email is valid.

Invalid Email
    else:
        print(f"'{email_input}' is NOT a valid email address.")
If the validation returns False, display an error message.

Entry Point Check
if __name__ == "__main__":
    main()
This ensures that main() only runs if the file is executed directly, not when imported as a module.
Good Python practice for script structure.


# Task - 4 : Calculator Program


