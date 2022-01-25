#Realizzare un programma con le seguenti funzioni:

#1 stampa, una funzione che stampa il contenuto di una lista passata come argomento V

#2 statistiche, una funzione che riceve una lista e, se una lista di interi, ne determina:
    #-somma
    #-media
    #-minimo
    #-massimo

#3 somma vettoriale, una funzione che riceve in ingresso 2 liste, determina se sono due liste di interi, se hanno la stessa dimensione e ne calcola la somma vettoriale, poi ritornata come lista, altrimenti ne torna una vuota

def my_fun(food):

        
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_fun(fruits)


def mia_funzione(numeri):

    for item in numeri:
        if isinstance(item,int):
            somma=sum(numeri)
            print("sum = ", somma)
        else:
            print('Elementi della lista non calcolabili')

    for item in numeri:
        if isinstance(item,int):
            avg=somma/len(numeri)
            print("average = ", avg)
        else:
            print('Elementi della lista non calcolabili')

    for item in numeri:
        if isinstance(item,int):

            mm= set( (x for x in range(min(numeri),max(numeri)+1)))
            print("min and max=",mm)

        else:
            print('Elementi della lista non calcolabili')


mia_funzione([1,2])

def _sum(l,t):

    somma = [x + y for x, y in zip(l,t)]
    if not True:
        for item in _sum:
            if isinstance(item,int):
                return True
            else:
                return False 

        if len(t)==len(l):
            return True
        else:
            return False

        print([''])
    else:
        print(somma)
        


_sum([28,20],[20,5])

    




