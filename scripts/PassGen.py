
#############
## CREDITS ##
#############

# PassGen.py Created by CBen-Judah
# Folder and it's contents can be found at - https://github.com/dwyl/english-words

########################
## PASSWORD GENERATOR ##
########################

import random

# Load a list of words from a file
with open("words.txt", "r") as f:
    words = [word.strip() for word in f.readlines()]

def generate_password(length):
    # Check if the desired password length is long enough to include at least one word pair and #1
    if length <= 2:
        raise ValueError("Password length must be at least 3 characters to include #1")
    
    # Choose random words from the list until the password length is reached
    password = ""
    while len(password) < length - 2:
        # Choose a random word that is at least as long as the remaining space
        remaining_space = length - len(password) - 2
        candidate_words = [word for word in words if len(word) >= remaining_space]
        if len(candidate_words) == 0:
            # If there are no words long enough, choose a random word from the original list
            word = random.choice(words)
        else:
            # Otherwise, choose a random word from the candidate list
            word = random.choice(candidate_words)
        password += word
    
    # Add #1 at the end of the password
    password += "#1"
    
    return password

# Example usage:
length = int(input("Enter desired password length: "))
password = generate_password(length)
print("Your new password is:", password)