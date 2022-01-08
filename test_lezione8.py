#creare un modello ricordandosi di creare le condizioni


import unittest
from prova import l

class test_lista_predizione(unittest.TestCase):
    l= [50,52,60]

    #test per n<2

    def test_n_min_2(self):

        
        n= len(self.l)

        self.assertEqual(n.len(n<2), n)

    #test per data != float

    def test_not_a_list(self):

        
        data= list(l)
        self.assertEqual(float(data),l)

        


    

        
            


            

        
    