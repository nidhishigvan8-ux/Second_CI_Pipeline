def count_words(text):
    
    if not text or text.isspace():
        return 0
    
    words = text.split()
    return len(words)