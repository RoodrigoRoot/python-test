import unittest
from user import ValidationUser

class ValidationNameTest(unittest.TestCase):
    
    def test_validate_name_is_correct(self):
        name = "Rodrigo"
        validation_name = ValidationUser.validate_name(name)
        self.assertIsNotNone(validation_name)
        self.assertEqual(validation_name, name)

    def test_validate_name_is_blank_fail(self):
        name = ""
        with self.assertRaises(ValueError):
            ValidationUser.validate_name(name)

    def test_validate_name_format_is_wrong(self):
        name = "R0dr1g0"
        with self.assertRaises(ValueError):
            ValidationUser.validate_name(name)

    def test_validate_name_length_greater_50_letters(self):
        name = "rodrigo"*50
        with self.assertRaises(ValueError):
            ValidationUser.validate_name(name)


class ValidationUsernameTest(unittest.TestCase):
    
    def test_validate_username_is_correct(self):
        username = "rodd"
        validation_username = ValidationUser.validate_username(username)
        self.assertIsNotNone(validation_username)
        self.assertEqual(validation_username, username)

    def test_validate_username_is_blank_fail(self):
        username = ""
        with self.assertRaises(ValueError):
            ValidationUser.validate_username(username)

    def test_validate_username_less_four_letters(self):
        username = "rod"
        with self.assertRaises(ValueError):
            ValidationUser.validate_username(username)

    def test_validate_username_length_greater_30_letters(self):
        username = "rodrigo"*30
        with self.assertRaises(ValueError):
            ValidationUser.validate_username(username)



class ValidationAgeTest(unittest.TestCase):
    
    def test_validate_age_is_correct(self):
        age = 26
        validation_age = ValidationUser.validate_age(age)
        self.assertIsNotNone(validation_age)
        self.assertEqual(validation_age, age)

    def test_validate_age_is_blank_fail(self):
        age = 0
        with self.assertRaises(ValueError):
            ValidationUser.validate_age(age)

    def test_validate_age_15_years_old_fail(self):
        age = 15
        with self.assertRaises(ValueError):
            ValidationUser.validate_age(age)

    def test_validate_age_is_string_fail(self):
        age = "26"
        with self.assertRaises(ValueError):
            ValidationUser.validate_age(age)
