import random
import string

def generate_shifts(length):
    """Generate a list of random shifts (1–26) for given length."""
    return [random.randint(1, 26) for _ in range(length)]

def encrypt(message):
    """Encrypt message with a one-time pad using random shifts."""
    message = message.lower()
    shifts = generate_shifts(len(message))
    encrypted_chars = []

    for char, shift in zip(message, shifts):
        if char in string.ascii_lowercase:  # only shift letters
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_chars.append(new_char)
        else:
            encrypted_chars.append(char)  # keep punctuation/space unchanged

    encrypted_message = "".join(encrypted_chars)
    return encrypted_message, shifts

def decrypt(encrypted_message, shifts):
    """Decrypt message using the provided shifts."""
    decrypted_chars = []
    for char, shift in zip(encrypted_message, shifts):
        if char in string.ascii_lowercase:
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_chars.append(new_char)
        else:
            decrypted_chars.append(char)
    return "".join(decrypted_chars)

# Example usage
if __name__ == "__main__":
    msg = input("Enter message: ")
    encrypted, shifts = encrypt(msg)
    print("Encrypted:", encrypted)
    print("Shifts used:", shifts)

    decrypted = decrypt(encrypted, shifts)
    print("Decrypted:", decrypted)

#tried to change the code
