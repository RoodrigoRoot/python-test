
class Calculadora:

    def __init__(self, file=None) -> None:
        self.file = file

    def suma(self, num1, num2):
        try:
            resultado = int(num1) + int(num2)
            self.save_data(f"El resultado es: {resultado}")
            return resultado
        except ValueError as err:
            self.save_data("Solo se permiten número, por favor revise.")
            return "Solo se permiten número, por favor revise."


    def resta(self, num1, num2):
        try:
            resultado =  int(num1) - int(num2)
            self.save_data(f"El resultado es: {resultado}")
            return resultado
        except ValueError as err:
            return "Solo se permiten número, por favor revise."

    def save_data(self, value):
        with open(self.file, "a+") as file:
            file.write(value+"\n")
