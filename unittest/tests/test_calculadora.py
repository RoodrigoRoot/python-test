import os
import unittest
from calculadora import Calculadora


class CalculadoraSumaTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.calculadora = Calculadora(file="prueba.txt")

    def test_suma_with_integers_succesfully(self):
        #Arrange
        num1 = 4
        num2 = 5
        resultado_expected = 9

        resultado = self.calculadora.suma(num1, num2)
        self.assertEqual(resultado, resultado_expected)

    def test_suma_with_strings_return_message(self):
        #Arrange
        num1_fail = "xfddsf"
        num2_fail = "123asddsa"
        message = "Solo se permiten número, por favor revise."
        
        #Act
        resultado = self.calculadora.suma(num1_fail, num2_fail)
        
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, message)

    def test_suma_with_numbers_strings(self):
        #Arrange
        num1_string = "1"
        num2_string="4"
        resultado_expected = 5
        
        #Act
        resultado = self.calculadora.suma(num1_string, num2_string)
        

        self.assertEqual(resultado, resultado_expected)

    def tearDown(self) -> None:
        file = os.getcwd()+"/prueba.txt"
        os.remove(file)

    @unittest.skip
    def test_example_create_user():
        #Arrange
        data_user = {...}
        
        #Act
        #create_user(data_user) # Pero internamente, también me crea una tarjeta

        #Assert
        #Verificar que el usuario se ha creado.
        # Verificar que su tarjeta, también se haya creado.



class CalculadoraRestaTest(unittest.TestCase):

    def test_resta_with_integers_succesfully(self):
        calculadora = Calculadora(file="prueba.txt")
        resultado = calculadora.resta(4, 5)
        self.assertEqual(resultado, -1)


# Ok
# Error -> La prueba no ha pasado. Y el resultado, en vez de ser una aserción, es un error
# Fail -> La prueba también falló, y se generó una excepción (AssertionError)