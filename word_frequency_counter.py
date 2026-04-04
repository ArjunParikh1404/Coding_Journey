# A simple Python program to count word frequencies in a given text input.

from collections import Counter
import re

def word_frequency(text):
    # Normalize text: lowercase + remove punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count frequencies
    return Counter(words)


if __name__ == "__main__":
    text = input("Enter text:\n")
    
    frequencies = word_frequency(text)
    
    # Print results sorted by frequency
    for word, count in frequencies.most_common():
        print(f"{word}: {count}")
