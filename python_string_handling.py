print("Hello, World!") # Output: Hello, World!

# To print quotes inside a string, you can use single quotes for the string and double quotes for the text, or vice versa.
print("'Hello, World'") # Output: 'Hello, World!'
print('Hello "World"') # Output: "Hello World"

english = "I'm learning Python!" # Output: I'm learning Python!
print(english)

#Multiple lines of text can be printed using triple quotes (''' or """)
multiline = """This is a multiline string.
Using triple double quotes."""
print(multiline)

multiline = '''This is another multiline string.
Using triple single quotes.'''
print(multiline)

# Length of a string can be found using the len() function.
word = "sternocleidomastoid"
print(len(word)) # Output: 19

# Check if a substring is in a string using the 'in' keyword.
phrase = "This is a course of Python fundamentals."
result = "Python" in phrase # Check if "Python" is in the phrase
print(result) # Output: True
result = "python" in phrase # Check if "python" (lowercase) is in the phrase (case-sensitive)
print(result) # Output: False

result = "JavaScript" not in phrase # Check if "JavaScript" is not in the phrase
print(result) # Output: True

# The upper() method converts all characters in the string to uppercase.
uppercase_phrase = phrase.upper() # Convert the phrase to uppercase
print(uppercase_phrase) # Output: THIS IS A COURSE OF PYTHON FUNDAMENTALS.

# The lower() method converts all characters in the string to lowercase.
lowercase_phrase = phrase.lower() # Convert the phrase to lowercase
print(lowercase_phrase) # Output: this is a course of python fundamentals.

# The capitalize() method capitalizes the first character of the string and converts the rest to lowercase.
capitalized_phrase = phrase.capitalize() # Capitalize the first character of the phrase
print(capitalized_phrase) # Output: This is a course of python fundamentals.

# The title() method capitalizes the first character of each word in the string and converts the rest to lowercase.
titlecase_phrase = phrase.title() # Convert the phrase to title case
print(titlecase_phrase) # Output: This Is A Course Of Python Fundamentals.

# The strip() method removes leading and trailing whitespace from the string.
spaces_text = "      This text has leading and trailing spaces.      "
print(spaces_text) # Output: "      This text has leading and trailing spaces.      "
print(len(spaces_text)) # Output: 54 (including spaces)

without_spaces_text = spaces_text.strip() # Remove leading and trailing spaces
print(without_spaces_text) # Output: "This text has leading and trailing spaces."
print(len(without_spaces_text)) # Output: 42 (without leading and trailing spaces)

spaces_text = "    '  This text has leading and trailing spaces. '  "
print(spaces_text) # Output: "    '  This text has leading and trailing spaces. '  "
print(len(spaces_text)) # Output: 53 (including spaces and quotes)
without_spaces_text = spaces_text.strip() # Remove leading and trailing spaces before and after the simple quotes
print(without_spaces_text) # Output: "'  This text has leading and trailing spaces. '"
print(len(without_spaces_text)) # Output: 47 (without leading and trailing spaces)