import pytest
import unittest

def inc(x):
    return x + 1


def test_inc():
    assert inc(3) == 4

def test_inc_with_strings():
    with pytest.raises(TypeError):
        inc("423")




# class IncTest(unittest.TestCase):

#     def test_inc(self):
#         resultado = inc(3)
#         self.assertEqual(resultado, 5)

