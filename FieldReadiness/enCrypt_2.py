import string

text = "Get this message to the main server"
shift = 13

# Create a placeholder list
encrypted_text = list(range(len(text)))


alphabet = string.ascii_lowercase
first_half = alphabet[:shift]
second_half = alphabet[shift:]
shifted_alphabet = second_half + first_half

for i, letter in enumerate(text.lower()):
    if letter in alphabet:
        # Find the original index position
        original_index = alphabet.index(letter)
        # Shifted letter
        new_letter = shifted_alphabet[original_index]
        encrypted_text[i] = new_letter

    # Punctuation or space
    else:
        encrypted_text[i] = letter

print(''.join(encrypted_text))
