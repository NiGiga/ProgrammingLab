import unittest
from lezione7 import CSVFile


#testing del name

class TestCSVFile(unittest.TestCase):

    def test_init(self):

        csv_file = CSVFile('shampoo_sales.csv')

        #controllo che il nome del file sia salvato
        #in un attributo del nome name

        self.assertEqual(csv_file.name, 'shampoo_sales.csv')

