def first_non_repeating_char(s: str):
    """
    Finds the first non-repeating character in a given string.
    Returns None if all characters repeat or if the string is empty.
    """
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    for char in s:
        if char_count[char] == 1:
            return char
            
    return None

if __name__ == "__main__":
    test_str = "swiss"
    result = first_non_repeating_char(test_str)
    print(f"First non-repeating character in '{test_str}' is: {result}")