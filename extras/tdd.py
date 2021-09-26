from typing import Type
import unittest


def suma(num1: int, num2: int) -> int:
    
    if type(num1) != int or type(num2) != int:
        raise TypeError("Solo se aceptan números enteros")
    return num1 + num2



class SumaTest(unittest.TestCase):
    
    def test_suma_succesfully(self):
        res = suma(4,9)
        self.assertEqual(res, 13)
        self.assertIsInstance(res, int)

    def test_suma_with_strings_fail(self):
        with self.assertRaises(TypeError):
            suma("4","9")

    def test_suma_with_float_fail(self):
        with self.assertRaises(TypeError):
            suma(4.5, 4.67)
