import re
import sys
from typing import Dict, List

class PasswordStrengthChecker:
    """
    A comprehensive password strength checker tool for internship activity.
    This tool evaluates password strength based on multiple security criteria.
    """

    def __init__(self):
        self.criteria = {
            'length': {
                'min_length': 8,
                'weight': 1,
                'description': 'At least 8 characters long'
            },
            'uppercase': {
                'pattern': r'[A-Z]',
                'weight': 1,
                'description': 'Contains uppercase letters (A-Z)'
            },
            'lowercase': {
                'pattern': r'[a-z]',
                'weight': 1,
                'description': 'Contains lowercase letters (a-z)'
            },
            'digits': {
                'pattern': r'\d',
                'weight': 1,
                'description': 'Contains numbers (0-9)'
            },
            'special_chars': {
                'pattern': r'[!@#$%^&*(),.?":{}|<>]',
                'weight': 1,
                'description': 'Contains special characters'
            }
        }

    def assess_password_strength(self, password: str) -> Dict:
        """
        Assess the strength of a password based on multiple criteria.

        Args:
            password (str): The password to assess

        Returns:
            Dict: Dictionary containing score, strength level, and feedback
        """
        if not password:
            return {
                "score": 0,
                "strength": "Invalid",
                "feedback": ["Password cannot be empty"]
            }

        feedback = []
        score = 0
        total_possible_score = sum(criterion['weight'] for criterion in self.criteria.values())

        # Check each criterion
        for criterion_name, criterion in self.criteria.items():
            if criterion_name == 'length':
                if len(password) >= criterion['min_length']:
                    score += criterion['weight']
                else:
                    feedback.append(f"Password should be {criterion['description']}.")
            else:
                if re.search(criterion['pattern'], password):
                    score += criterion['weight']
                else:
                    feedback.append(f"Password should include {criterion['description']}.")

        # Determine strength level
        strength_percentage = (score / total_possible_score) * 100

        if strength_percentage >= 100:
            strength = "Very Strong"
        elif strength_percentage >= 80:
            strength = "Strong"
        elif strength_percentage >= 60:
            strength = "Moderate"
        elif strength_percentage >= 40:
            strength = "Weak"
        else:
            strength = "Very Weak"

        return {
            "score": score,
            "max_score": total_possible_score,
            "strength": strength,
            "percentage": strength_percentage,
            "feedback": feedback
        }

    def generate_strong_password(self, length: int = 12) -> str:
        """
        Generate a strong password with the specified length.

        Args:
            length (int): Desired password length (default: 12)

        Returns:
            str: Generated strong password
        """
        import random
        import string

        if length < 8:
            length = 8

        # Ensure at least one character from each category
        lowercase = random.choice(string.ascii_lowercase)
        uppercase = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        special = random.choice("!@#$%^&*(),.?\":{}|<>")

        # Fill remaining length with random characters
        remaining_length = length - 4
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>"
        remaining_chars = ''.join(random.choice(all_chars) for _ in range(remaining_length))

        # Combine all parts and shuffle
        password_chars = list(lowercase + uppercase + digit + special + remaining_chars)
        random.shuffle(password_chars)

        return ''.join(password_chars)

    def check_common_passwords(self, password: str) -> bool:
        """
        Check if password is in a list of common passwords.

        Args:
            password (str): Password to check

        Returns:
            bool: True if password is common, False otherwise
        """
        common_passwords = {
            'password', '123456', 'password123', 'admin', 'qwerty',
            'letmein', 'welcome', 'monkey', '123456789', 'password1',
            'abc123', '12345678', 'qwerty123', '111111', '1234567',
            'sunshine', 'iloveyou', 'princess', 'rockyou', '123123'
        }

        return password.lower() in common_passwords

def print_colored_output(result: Dict):
    """
    Print colored output based on password strength.
    """
    colors = {
        "Very Strong": "\033[92m",  # Green
        "Strong": "\033[94m",       # Blue
        "Moderate": "\033[93m",     # Yellow
        "Weak": "\033[91m",         # Red
        "Very Weak": "\033[91m",    # Red
        "Invalid": "\033[95m"       # Magenta
    }

    reset_color = "\033[0m"

    strength = result['strength']
    color = colors.get(strength, "\033[0m")

    print(f"\n{'='*50}")
    print("PASSWORD STRENGTH ANALYSIS")
    print(f"{'='*50}")
    print(f"Strength: {color}{strength}{reset_color}")
    print(f"Score: {result['score']}/{result['max_score']} ({result['percentage']:.1f}%)")

    if result['feedback']:
        print(f"\n{color}IMPROVEMENT SUGGESTIONS:{reset_color}")
        for suggestion in result['feedback']:
            print(f"• {suggestion}")

    print(f"{reset_color}")

def main():
    """
    Main function to run the password strength checker.
    """
    print("🔐 PASSWORD STRENGTH CHECKER - INTERNSHIP ACTIVITY")
    print("=" * 55)

    checker = PasswordStrengthChecker()

    while True:
        print("\nChoose an option:")
        print("1. Check password strength")
        print("2. Generate a strong password")
        print("3. Exit")

        try:
            choice = input("\nEnter your choice (1-3): ").strip()

            if choice == '1':
                password = input("Enter password to check: ").strip()

                # Check for common passwords
                if checker.check_common_passwords(password):
                    print("⚠️  WARNING: This password is commonly used and easily guessable!")

                result = checker.assess_password_strength(password)
                print_colored_output(result)

            elif choice == '2':
                try:
                    length = int(input("Enter desired password length (minimum 8): "))
                    if length < 8:
                        print("Password length set to minimum of 8 characters.")
                        length = 8

                    generated_password = checker.generate_strong_password(length)
                    print(f"\n🔑 Generated Password: {generated_password}")

                    # Check the generated password strength
                    result = checker.assess_password_strength(generated_password)
                    print("Generated password strength:")
                    print_colored_output(result)

                except ValueError:
                    print("❌ Invalid input. Please enter a number.")

            elif choice == '3':
                print("👋 Thank you for using the Password Strength Checker!")
                sys.exit(0)

            else:
                print("❌ Invalid choice. Please select 1, 2, or 3.")

        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Thank you for using the Password Strength Checker!")
            sys.exit(0)
        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
