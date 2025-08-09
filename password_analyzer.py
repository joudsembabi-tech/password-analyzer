import re
import random
import string

def analyze_password_strength(password):
    """
    Analyze the strength of a given password and return a score + message.
    Criteria:
        - Length >= 8
        - Contains lowercase, uppercase, digits, and special characters
    """
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength evaluation
    if score == 5:
        return "🔒 Strong", "Your password is strong. Great job!"
    elif 3 <= score < 5:
        return "🟡 Medium", "Your password is okay, but could be stronger: " + "; ".join(feedback)
    else:
        return "🔴 Weak", "Weak password: " + "; ".join(feedback)


def generate_secure_password(length=12):
    """
    Generate a secure random password containing:
    - Uppercase
    - Lowercase
    - Digits
    - Special characters
    """
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))


if _name_ == "_main_":
    print("=== Password Strength Analyzer ===")
    user_password = input("Enter a password to analyze: ")
    strength, message = analyze_password_strength(user_password)
    print(f"Strength: {strength}")
    print(message)

    print("\nDo you want to generate a secure password? (y/n)")
    if input().lower() == 'y':
        new_password = generate_secure_password()
        print(f"Generated Secure Password: {new_password}")