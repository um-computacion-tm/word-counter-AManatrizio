import unittest


def diccionario(quote):
    for word in quote:
        resultado =  1 + quote.count(" ")
        
    
    return resultado






class diccionario(unittest.TestCase):
    def test_uno(self):
        resultado = diccionario('hola')
        self.assertEqual(resultado, 1)


if __name__ == '__main__':
    unittest.main()
