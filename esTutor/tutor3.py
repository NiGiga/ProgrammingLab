#estendere la classe CSVFile con i seguenti medoti:

#-get_date_vendite(): questa funzione ritornerà una lista con le date   delle vendite(Hinit, usare la fun creata nell'es2)
#-__str__(): questa funzione tornerà una header del file
from datetime import datetime 
#creo classe
class CSVFile():
    def __init__(self, name):
        self.name = name

    def __str__():
        return 'Date vendite'
    #creo la funzione
    def get_data(self):
        my_file = open(self.name, 'r')
        #creo una lista vuoto
        values = []
        #splitto sulla virgola
        for line in my_file:
            elemnts = line.split(',')
            if elemnts[0] != 'Date':
                values.append(float(elemnts[1]))
        #chiudo il file
        my_file.close()
        #ritorno i valori
        return (values)

    def get_date_vendite(self):
        my_file = open(self.name, 'r')
        dates = []
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                data = datetime.strptime(elements[0], '%d-%m-%Y')
                dates.append(data)
        my_file.close()
        return dates

#attribuisco a my_file CSVFile
my_file = CSVFile('shampoo_sales.csv')
#attribuisco a my_data la funzione
my_data = my_file.get_data()
#stampo a schermo i valori
print(my_data)

date_vendite = my_file.get_date_vendite()
for data in date_vendite:
    print(data.strftime('%d-%m-%Y'))