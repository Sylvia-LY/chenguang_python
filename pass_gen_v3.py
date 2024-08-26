import argparse
import random
import string

def generate_strong_password(length=8):
    # ensure the length is at least 8
    length = max(8, length)

    password = []
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    characters = string.ascii_letters+string.digits+string.punctuation
    remaining_length = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining_length))

    # prevent predictable patterns
    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='generate a strong random password')
    parser.add_argument('-l', '--length', type=int, default=8, help='length of the password (minimum 8 characters)')
    args = parser.parse_args()

    print(f"generated strong password: {generate_strong_password(args.length)}")