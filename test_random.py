import unittest
import random
from function import search_key  
from oracle import oracle_search  

class TestRandomSearch(unittest.TestCase):
    def test_random_generation(self):
        random.seed(42) 
        N = 100 
        
        for _ in range(N):
            
            v = [random.randint(-10, 10) for _ in range(5)]
            
            key = random.randint(-10, 10)
            
            
            expected = oracle_search(v, key)
            actual = search_key(v, key)
            
            #compara rezultatele asteptate cu cele actuale. daca nu sunt egale afiseaza mesaj de eroare 
            self.assertEqual(actual, expected, f"Esec pentru v={v}, key={key}") 
if __name__ == '__main__':
    unittest.main()