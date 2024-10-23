#!/usr/bin/python3

def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these characters: ., ? and :
    
    Parameters:
    text (str): The input text to process

    Raises:
    TypeError: If the input text is not a string
    """
    
    # Check if the input is a string, if not raise TypeError
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a string to store the result
    result = ""

    # Iterate over each character in the text
    for char in text:
        result += char
        # If character is one of '.', '?', or ':', add two newlines
        if char in ['.', '?', ':']:
            result += "\n\n"
    
    # Print the result with each line stripped of leading/trailing spaces
    for line in result.split("\n"):
        print(line.strip(), end="")
        if line.strip():  # Add the newline only if line is not empty
            print()

