import re

def assess_password_strength(password: str) -> dict:
    """
    Assess the strength of a password based on criteria:
    - length >= 8
    - contains uppercase letters
    - contains lowercase letters
    - contains digits
    - contains special characters

    Returns a dictionary with score and feedback.
    """
    feedback = []
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }

    strength = strength_levels.get(score, "Very Weak")

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

def main():
    password = input("Enter a password to assess its strength: ")
    result = assess_password_strength(password)
    print(f"Password Strength: {result['strength']} (Score: {result['score']}/5)")
    if result['feedback']:
        print("Feedback:")
        for item in result['feedback']:
            print(f"- {item}")

if __name__ == "__main__":
    main()
