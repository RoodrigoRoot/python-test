import unittest
from user import User
from uuid import UUID


class NameUserTest(unittest.TestCase):

    def test_create_user_name_succesfully(self):
        user = User("Rodrigo", "rodd", 26)
        user_saved = user.create()
        self.assertIsNotNone(user_saved)
        self.assertIsInstance(user_saved.id, UUID)

    def test_create_user_fail_name_is_wrong(self):
        with self.assertRaises(ValueError):
            User("Rodr1g0", "rodd", 26)

    def test_create_user_fail_name_is_blank(self):
        with self.assertRaises(ValueError):
            User("", "rodd", 26)

    def test_create_user_fail_name_greater_than_50_letters(self):
        with self.assertRaises(ValueError):
            User("Rodrigo"*50, "rodd", 26)


class UsernameUserTest(unittest.TestCase):

    def test_create_username_succesfully(self):
        user = User("Rodrigo", "rodd", 26)
        user_saved = user.create()
        self.assertIsNotNone(user_saved)
        self.assertIsInstance(user_saved.id, UUID)

    def test_create_user_sername_less_thant_four_letters_fail(self):
        with self.assertRaises(ValueError):
            User("Rodrigo", "rod", 26)

    def test_create_user_username_is_blank_fail(self):
        with self.assertRaises(ValueError):
            User("Rodrigo", "", 26)

    def test_create_user_username_greater_than_30_letters_fail(self):
        with self.assertRaises(ValueError):
            User("Rodrigo", "rodd"*30, 26)


class AgeUserTest(unittest.TestCase):

    def test_create_user_age_succesfully(self):
        user = User("Rodrigo", "rodd", 26)
        user_saved = user.create()
        self.assertIsNotNone(user_saved)
        self.assertIsInstance(user_saved.id, UUID)

    def test_create_user_age_15_years_old_fail(self):
        with self.assertRaises(ValueError):
            User("Rodrigo", "rodd", 15)

    def test_create_username_is_blank_fail(self):
        with self.assertRaises(ValueError):
            User("Rodrigo", "rodd", 0)

    def test_create_user_age_is_string_fail(self):
        with self.assertRaises(ValueError):
            User("Rodrigo", "rodd", "26")
