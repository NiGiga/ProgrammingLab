#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista  di liste, ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ] Provatelo sul file “shampoo_sales.csv”.

#creo classe
class CSVFile():
    def __init__(self, name):
        self.name = name
    #creo la funzione
    def get_data(self):
        my_file = open(self.name, 'r')
        #creo una lista vuoto
        values = []
        #splitto sulla virgola
        for line in my_file:
            elemnts = line.split(',')
             #if(!='Data')
            values.append(elemnts)
        #chiudo il file
        my_file.close()
        #ritorno i valori
        return (values)
#attribuisco a shampoo CSVFile
shampoo = CSVFile('shampoo_sales.csv')
#attribuisco a my_data la funzione
my_data = shampoo.get_data()
#stampo a schermo i valori
print(my_data)





    
