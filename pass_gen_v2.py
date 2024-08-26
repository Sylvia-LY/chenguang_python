import random
import string

def is_password_strong(user_password):
    strength_flags = 0b00000

    for i in user_password:
        if i.isupper():
            strength_flags |= 0b10000
        elif i.islower():
            strength_flags |= 0b01000
        elif i.isdigit():
            strength_flags |= 0b00100
        elif i in string.punctuation:
            strength_flags |= 0b00010

    if len(user_password)>=8:
        strength_flags |= 0b00001
    
    if strength_flags==0b11111:
        return "your password is valid."
    else:
        missing_criteria = []
        if strength_flags & 0b00001 == 0:
            missing_criteria.append("at least 8 characters")
        if strength_flags & 0b10000 == 0:
            missing_criteria.append("at least 1 uppercase letter")
        if strength_flags & 0b01000 == 0:
            missing_criteria.append("at least 1 lowercase letter")
        if strength_flags & 0b00100 == 0:
            missing_criteria.append("at least 1 digit")
        if strength_flags & 0b00010 == 0:
            missing_criteria.append("at least 1 special character")

        return "password must contain " + ", ".join(missing_criteria) + "."

# 密码强度随机，有可能不合格
def generate_password(length=8):
    characters = string.ascii_letters \
        + string.digits \
        + string.punctuation
    # list comprehension
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    while 1:
        password = generate_password()
        if is_password_strong(password)=="your password is valid.":
            break
    print(f"generated a strong password: {password}")