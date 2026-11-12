import re
import getpass

COMMON_PASSWORDS = [
    "password", "123456", "12345678",
    "qwerty", "admin", "password123"
]


def check_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    # Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append("Avoid commonly used passwords.")

    # Display strength
    print("\n===== PASSWORD SECURITY REPORT =====")

    if score <= 2:
        print("Strength: WEAK")
    elif score <= 4:
        print("Strength: MEDIUM")
    else:
        print("Strength: STRONG")

    print("Security Score:", score, "/ 6")

    if suggestions:
        print("\nSuggestions:")
        for item in suggestions:
            print("-", item)
    else:
        print("\nExcellent! All basic security checks passed.")

    print("\nNote: This is a basic educational checker.")
    print("It does not guarantee password security.")


def main():
    print("====================================")
    print("     PASSWORD STRENGTH CHECKER")
    print("====================================")

    # Use input() while testing so you can see what you type
    password = input("Enter a test password: ")

    check_password(password)


if __name__ == "__main__":
    main()