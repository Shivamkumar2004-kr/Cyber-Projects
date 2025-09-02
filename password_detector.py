import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count total errors
    errors = sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    if errors == 0:
        strength = "💪 Strong Password"
    elif errors <= 2:
        strength = "👌 Moderate Password"
    else:
        strength = "❌ Weak Password"

    # Detailed feedback
    feedback = []
    if length_error:
        feedback.append("🔸 At least 8 characters")
    if digit_error:
        feedback.append("🔸 Include a number")
    if uppercase_error:
        feedback.append("🔸 Include an uppercase letter")
    if lowercase_error:
        feedback.append("🔸 Include a lowercase letter")
    if symbol_error:
        feedback.append("🔸 Include a special character (!@#$ etc.)")

    return strength, feedback


# --- Main ---
if __name__ == "__main__":
    password = input("Enter your password to check strength: ")
    strength, suggestions = check_password_strength(password)
    
    print("\nPassword Strength:", strength)
    if suggestions:
        print("Suggestions to improve:")
        for s in suggestions:
            print(s)
