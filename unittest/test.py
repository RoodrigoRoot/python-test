import unittest
from tests import test_calculadora
from tests import test_factorial

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_calculadora))
    suite.addTests(loader.loadTestsFromModule(test_factorial))
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)

# Verbosity
# Tres valores: 0 (Total de tests y tiempo), 1 (Total de tests, puntos, fallidos, errores y tiempo)
# 2 (Total de tests, puntos, fallidos, errores, tiempo, resultado y el nombre y ubicación de los tests que se ejecutaron)