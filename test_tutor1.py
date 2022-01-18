#Realizzare un programma con le seguenti funzioni:

#1 stampa, una funzione che stampa il contenuto di una lista passata come argomento

#2 statistiche, una funzione che riceve una lista e, se una lista di interi, ne determina:
    #-somma
    #-media
    #-minimo
    #-massimo

#3 somma vettoriale, una funzione che riceve in ingresso 2 liste, determina se sono due liste di interi, se hanno la stessa dimensione e ne calcola la somma vettoriale, poi ritornata come lista, altrimenti ne torna una vuota

import unittest

class lista(unittest.TestCase):
     def TestLista(self):
         self.