import unittest
from tests import test_user
from tests import test_validations

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_user))
    suite.addTests(loader.loadTestsFromModule(test_validations))
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)
