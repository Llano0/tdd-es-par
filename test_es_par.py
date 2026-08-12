import unittest
from math_utils import es_par 

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4))

    def test_10000000000001_no_es_par(self):
        self.assertFalse(es_par(10000000000001))
    
    def test_10_es_par(self):
        self.assertTrue(es_par(10))

if __name__ == "__main__":
    unittest.main()