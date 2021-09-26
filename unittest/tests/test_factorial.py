import unittest
from factorial import factorial

class FactorialTest(unittest.TestCase):
    
    def test_factorial_with_intenger(self):
        resultado = factorial(5)
        self.assertEqual(resultado, 120)

    def test_factorial_with_strings_raise_excepction(self):
        with self.assertRaises(TypeError):
            factorial("2132132123retwgsdfg")