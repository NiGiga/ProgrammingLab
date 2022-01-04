# Modificate l’oggetto CSVFile della lezione precedente in modo che stampi a schermo un messaggio di errore se si cerca di aprire un file non esistente.

#==============================
#  Classe per file CSV
#==============================

class CSVFile():
    #creo la classe
    def __init__(self, name):
        #setto il nome del file
        self.name=name
        #provo ad aprire il file e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read=False
            print('Errore in apertura del file "{}"'.format(e))

    def get_data(self):
        if not self.can_read:
            print('Errore, file non aperto o illegibile')
            #esco dalla funzione tornando niente
            return None

        else:
            #inizializzo una lista vuota
            data=[]
            #apro il file
            my_file = open(self.name,'r')
            #leggo il file linea per linea
            for line in my_file:
                #faccio lo split di ogni elemento sulla virgola
                elements = line.split(',')
                #pulisco il carattere di newline con strip
                elements[-1]= elements[-1].strip() 
                #se non processo l'intestazione
                if elements[0] != 'Date':
                    #aggiungo allalista gli elementi
                    data.append(elements)
            #chiudo il file        
            my_file.close()
            #ritorno data
            return data       
                                            
            
#==============================
# Classe per file NumericalCSV
#============================== 
           
class NumericalCSV(CSVFile):

    def get_data(self):
        #chiamo la get_data del genitore
        string_data= super().get_data()
        #preparo la lista per contenere i file in formato numerico
        numerical_data = []
        #ciclo su tutte le righe corrisondenti al file
        for string_row in string_data:
            #preparo una lista di supporto per salvre il
            #file in formato numerico(escluso il primo elemento)
            numerical_row = []

            # Ciclo su tutti gli elementi della riga con un
            # enumeratore: cosi' ho gratis l'indice "i" della
            # posizione dell'elemento nella riga.
            for i, element in enumerate(string_row):
                if i==0:
                    #il primo elemento lo lascio in formato stringa
                    numerical_row.append(element)
                else:
                    #converto a float tutti gli altri ma se non ci riesco
                    #stampo l'errore e rompo il ciclo.(poi salterò la riga)
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore di conversione del valore"{}" a numerico: "{}"'.format(element,e))
                        break
            # Alla fine aggiungo la riga in formato numerico alla lista
            # "esterna", ma solo se sono riuscito a processare tutti gli
            # elementi. Qui controllo per la lunghezza, ma avrei anche potuto
            # usare una variabile di supporto o fare due break in cascata.
            if len(numerical_row)==len(string_row):
                numerical_data.append(numerical_row)          
        return numerical_data            
            
#==============================
#  Corpo del programma
#==============================

mio_file = CSVFile('shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: {}'.format(mio_file.get_data()))

mio_file_numerico = NumericalCSV(name= 'shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file_numerico.name))
print('Dati contenuti nel file: {}'.format(mio_file_numerico.get_data()))




            
            
        
        
        
                    
            
                

