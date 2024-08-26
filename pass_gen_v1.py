import string
import pyperclip

def check_password_strength(user_password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for i in user_password:
        if i in string.ascii_uppercase:
            has_upper = True
        elif i in string.ascii_lowercase:
            has_lower = True
        elif i in string.digits:
            has_digit = True
        elif i in string.punctuation:
            has_special = True

    # store feedback
    prompt = []

    # check each criterion and add feedback if necessary
    if len(user_password)<8:
        prompt.append("at least 8 characters")
    if not has_upper:
        prompt.append("at least 1 uppercase letter")
    if not has_lower:
        prompt.append("at least 1 lowercase letter")
    if not has_digit:
        prompt.append("at least 1 digit")
    if not has_special:
        prompt.append("at least 1 special character")

    if not prompt:
        pyperclip.copy(user_password)
        return "your password is valid and has been copied to the clipboard."

    return "password must contain " + ", ".join(prompt) + "."

if __name__ == "__main__":
    user_password = input("enter a password to check its strength: ")
    print(check_password_strength(user_password))