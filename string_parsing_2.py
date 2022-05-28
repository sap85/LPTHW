from string import ascii_lowercase
"""
Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of lowercase letters, find the sum of the values of the letters in the string.

lettersum("") => 0
lettersum("a") => 1
lettersum("z") => 26
lettersum("cab") => 6
lettersum("excellent") => 100
lettersum("microspectrophotometries") => 317
"""

def calculate_letter_sum(word: str) -> int:
    letter_to_value = {l:v for v,l in enumerate(ascii_lowercase,start=1)}
    return sum(letter_to_value[letters] for letters in word)


calculate_letter_sum('microspectrophotometries')
