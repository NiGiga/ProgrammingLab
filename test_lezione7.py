import unittest
from lezione7 import CSVFile
from lezione7 import NumericalCSV

    
        





class Testget_nomeCSVFile(unittest.TestCase):

    def test_nome(self):

        csv_file=CSVFile('shampoo_sales.csv')

        self.assertEqual(csv_file.name, 'shampoo_sales.csv')



class Testget_nomeNumericalCSVFile(unittest.TestCase):

    def test_nome(self):

        numcsv_file=NumericalCSV('shampoo_sales.csv')

        self.assertEqual(numcsv_file.name, 'shampoo_sales.csv')



