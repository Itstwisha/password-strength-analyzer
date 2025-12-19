import math
import re

# Load Dictionary Words
with open("data/common_passwords.txt", "r") as f:
    common_words = set(line.strip().lower() for line in f)

def entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[^A-Za-z0-9]", password): charset += 32

    return len(password) * math.log2(charset) if charset else 0

def evaluate_password(pw):
    issues = []

    # Length check
    if len(pw) < 8:
        issues.append("Too short (<8 chars)")

    # Dictionary check
    if pw.lower() in common_words:
        issues.append("Common password found in dictionary")

    # Pattern checks
    if pw.isdigit():
        issues.append("Only numbers")
    if pw.isalpha():
        issues.append("Only letters")

    ent = entropy(pw)

    # Strength logic
    if ent < 28:
        strength = "Weak"
    elif ent < 45:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, ent, issues

if __name__ == "__main__":
    pw = input("Enter password to analyze: ")
    strength, ent, issues = evaluate_password(pw)

    print("\nPassword Strength:", strength)
    print("Entropy Score:", round(ent, 2))
    print("Issues Found:")
    if issues:
        for i in issues:
            print("-", i)
    else:
        print("No major issues detected.")
