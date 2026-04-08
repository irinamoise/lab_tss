import unittest
from function import search_key

class TestSearchKey(unittest.TestCase):

    # testare functionala
    
    # partitionare de echivalenta

    """ 
    1. lungimea vectorului:

        - N1: lungime valida (5 elemente)
        - N2: lungime prea mica (<5 elem; returneaza mesaj de eroare)
        - N3: lungime prea mare (>5 elem; returneaza mesaj de eroare)

    2. rezultatul cautarii:
        - C1: elem key se afla in vector (returneaza indexul)
        - C2: elem nu se afla in vector (returneaza -1)

     """
    

    def test_equivalence_partitioning(self):
        # N1C1
        self.assertEqual(search_key([1, 2, 3, 4, 5], 3), 2)
        # N1C2
        self.assertEqual(search_key([1, 2, 3, 4, 5], 10), -1)
        # N2
        self.assertEqual(search_key([1, 2], 1), "Array length must be 5")
        # N3
        self.assertEqual(search_key([1, 2, 3, 4, 5, 6], 1), "Array length must be 5")

    # analiza val de frontiera
    
    """
    1. frontiere lungime: 4, 5, 6
    2. frontiere index: 0, 4 (pt elemente valide), -1 (pt elemente invalide)


    """
    def test_boundary_value_analysis(self):
       # cheia pe prima poz
        self.assertEqual(search_key([9, 1, 2, 3, 4], 9), 0)

        # cheia pe ultima poz
        self.assertEqual(search_key([1, 2, 3, 4, 9], 9), 4)

        # lungime la frontiera inferioara (4 elem)
        self.assertEqual(search_key([1, 2, 3, 4], 1), "Array length must be 5")

        # lungime la frontiera valida (5 elem)
        self.assertEqual(search_key([1, 2, 3, 4, 5], 1), 0)

        # lungime la frontiera superioara (6 elem)
        self.assertEqual(search_key([1, 2, 3, 4, 5, 6], 1), "Array length must be 5")

    
    #testare structurala

    #statement coverage

    def test_statement_coverage(self):
        # ramura de eroare lungime (instructiunile 1 si 2)
        search_key([1], 1) 
        # interiorul loop-ului si gasirea elem (instructiunile 1, 3, 4, null, 5)
        #search_key([1, 2, 3, 4, 5], 2)
        # finalul metodei si return -1 (instruct 1, 3, 4, null, 6)
        search_key([1, 2, 3, 4, 5], 99)


    # testarea circuitelor independente 
    """
    identifica setul de bază de căi liniar independente
    V(G) = e - n + 2 = 8- 7 +2 =3
    """

    def test_circuit_coverage(self):
        # 1: eroare la verificarea lungimii 
        self.assertIn("Array length must be 5", search_key([1, 2], 1))
        # 2: succes (gasit) 
        self.assertEqual(search_key([1, 2, 3, 4, 5], 5), 4)
        # 3: element negasit
        self.assertEqual(search_key([1, 2, 3, 4, 5], 0), -1)



if __name__ == '__main__':
    unittest.main()