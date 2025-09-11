import unittest
from password_strength_checker import assess_password_strength

class TestPasswordStrengthChecker(unittest.TestCase):

    def test_all_criteria_met(self):
        password = "Abcdef1!"
        result = assess_password_strength(password)
        self.assertEqual(result['score'], 5)
        self.assertEqual(result['strength'], "Very Strong")
        self.assertEqual(len(result['feedback']), 0)

    def test_missing_length(self):
        password = "Ab1!"
        result = assess_password_strength(password)
        self.assertLess(result['score'], 5)
        self.assertIn("Password should be at least 8 characters long.", result['feedback'])

    def test_missing_uppercase(self):
        password = "abcdef1!"
        result = assess_password_strength(password)
        self.assertLess(result['score'], 5)
        self.assertIn("Password should include at least one uppercase letter.", result['feedback'])

    def test_missing_lowercase(self):
        password = "ABCDEF1!"
        result = assess_password_strength(password)
        self.assertLess(result['score'], 5)
        self.assertIn("Password should include at least one lowercase letter.", result['feedback'])

    def test_missing_digit(self):
        password = "Abcdefg!"
        result = assess_password_strength(password)
        self.assertLess(result['score'], 5)
        self.assertIn("Password should include at least one number.", result['feedback'])

    def test_missing_special_char(self):
        password = "Abcdefg1"
        result = assess_password_strength(password)
        self.assertLess(result['score'], 5)
        self.assertIn("Password should include at least one special character.", result['feedback'])

    def test_empty_password(self):
        password = ""
        result = assess_password_strength(password)
        self.assertEqual(result['score'], 0)
        self.assertEqual(result['strength'], "Very Weak")
        self.assertEqual(len(result['feedback']), 5)

if __name__ == "__main__":
    unittest.main()
