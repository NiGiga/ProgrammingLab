# Parte 1 - Modificare l’oggetto CSVFile della lezione precedente in modo che alzi un'eccezione se il nome del file non è una stringa.
# Parte 2 - Modificare la funzione get_data di CSVFile in modo da leggere solo un intervallo di righe del file, aggiungendo gli argomenti start ed end opzionali, controllandone la correttezza e sanitizzandoli se serve. Infine, eseguire commit del file. 

# ==============================
#           CLASSI
# ==============================
#       Classe per CSVFile
# ==============================
class CSVFile():
    
    def __init__(self, name):
        # Istanziamento dell'attributo "name"
        self.name = name
        # Controllo del tipo di nome del file
        if type(name) != str:
            raise TypeError('Errore di tipo: il nome inserito non è una stringa! Ecco il parametro che lo ha generato: {}'.format(name))
    
    def get_data(self, start = None, end = None):
        # Istanziamento di due liste: una lista e una lista di lista
        list = []
        listoflist = []
        # Apertura del file
        try:
            file = open(self.name, 'r')
        except FileNotFoundError:
            print ('Il file che si sta cercando di aprire non esiste!')
            return None
        # Controllo della correttezza di start ed end
        if type(start) != int:
            raise TypeError('Errore di tipo: il parametro start={} inserito non è un numero intero!'.format(start))
        if type(end) != int:
            raise TypeError('Errore di tipo: il parametro end={} inserito non è un numero intero!'.format(end))
        if(start > 39):
            raise ValueError('Il parametro start={} è maggiore della lunghezza del file! Il file {} ha {} righe'.format(start, self.name, 39))
        if(end > 74):
            raise ValueError('Il parametro end={} è maggiore della lunghezza del file! Il file {} ha {} righe'.format(end, self.name, 39))
        if(start < 0):
            raise ValueError('Errore di valore (start={}): non è accettabile un valore negativo!'.format(start))
        if(end < 0):
            raise ValueError('Errore di valore (end={}): non è accettabile un valore negativo!'.format(end))
        if(start > end):
            raise ValueError('Il parametro start={} è maggiore del parametro end={}'.format(start, end))
        # Lettura del file, linea per linea
        for line in file:
            # Istanziamento di elementi con split di ogni riga su ","
            elements = line.split(',')
            # Eliminazione di caratteri indesiderati (newline e spazi)
            elements[-1] = elements[-1].strip()
            # Se non si processa l'intestazione, aggiunta degli elementi alla lista
            if elements[0] != 'Date':
                list.append(elements)
        # Chiusura del file
        file.close()
        # Aggiunta degli elementi della lista alla lista di lista
        listoflist.extend(list)
        return listoflist[start : end]
        
# ==============================
#   Classe per NumericalCSVFile
# ==============================
class NumericalCSVFile(CSVFile):

    def get_data(self, start = None, end = None):
        # Richiamo del metodo genitore
        string_data = super().get_data(start, end)
        # Istanziamento di una lista per salvare i valori
        numerical_data = []
        # Lettura del file, linea per linea
        for string_row in string_data:
            numerical_row = []
            for i, element in enumerate(string_row):
                if i == 0:
                    numerical_data.append(element)
                else:
                    try:
                        numerical_data.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
                if len(numerical_row) == len(string_row):
                    numerical_data.append(numerical_row)
        return numerical_data[start : end]

# ==============================
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
my_file = CSVFile(name = 'shampoo_sales.csv')
print('Nome del file: {}'.format(my_file.name))
print('Dati contenuti nel file: "{}"'.format(my_file.get_data(0, 39)))

my_numerical_file = NumericalCSVFile(name = 'shampoo_sales.csv')
print('Nome del file numerico: "{}"'.format(my_numerical_file.name))
print('Dati contenuti nel file numerico: "{}"'.format(my_numerical_file.get_data(0, 74)))