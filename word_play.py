def is_valid_identifier(word):
    """Check if a word is a valid Python identifier."""
    if not word:
        return False
    if not (word[0].isalpha() or word[0] == '_'):
        return False
    return all(c.isalnum() or c == '_' for c in word)

def is_palindrome(word):
    """Check if a word is a palindrome."""
    return word == word[::-1]

def main():
    # Get the initial word from the user
    word = input("Enter a word: ")
    
    # Print the length of the word
    print(f"Length of word: {len(word)}")
    
    # Print uppercase and lowercase versions
    print(f"Uppercase: {word.upper()}")
    print(f"Lowercase: {word.lower()}")
    
    # Count occurrences of a letter
    letter = input("Enter a letter: ")
    count = word.count(letter)
    print(f"'{letter}' appears {count} time(s) in '{word}'")
    
    # Count occurrences of a substring
    substring = input("Enter a substring: ")
    count = word.count(substring)
    print(f"'{substring}' appears {count} time(s) in '{word}'")
    
    # Reverse the word
    print(f"Reverse: {word[::-1]}")
    
    # Slice the word
    try:
        start = int(input("Enter a starting index: "))
        end = int(input("Enter an ending index: "))
        print(f"Sliced word: {word[start:end]}")
    except ValueError:
        print("Please enter valid integer indices")
    
    # Replace character
    char_to_replace = input("Enter a character to replace: ")
    replacement_char = input("Enter the replacement character: ")
    print(f"Replaced: {word.replace(char_to_replace, replacement_char, 1)}")
    
    # Concatenate with another word
    second_word = input("Enter a second word: ")
    print(f"Concatenated: {word + second_word}")
    
    # Check if palindrome
    print(f"Is a palindrome? {'Yes' if is_palindrome(word) else 'No'}")
    
    # Check if valid Python identifier
    print(f"Is a valid Python identifier? {'Yes' if is_valid_identifier(word) else 'No'}")

if __name__ == "__main__":
    main() 