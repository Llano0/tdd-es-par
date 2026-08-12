import unittest
from math_utils import es_multiplo

class TestEsMultiplo(unittest.TestCase):
    def test_4_es_multiplo_de_2(self):
        self.assertTrue(es_multiplo(4,2))

    def test_1000000000000_es_multiplo_de_5(self):
        self.assertTrue(es_multiplo(1000000000000,5))
    
    def test_10_es_multiplo_de_10(self):
        self.assertFalse(es_multiplo(10,11))

if __name__ == "__main__":
    unittest.main()