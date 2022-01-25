#Vogliamo calcolare la differenza degli elementi di una lista
#Aggiungeremo anche un parametro di nome “ratio”, che permetta di riscalare le differenze (ovvero la differenza tra gli elementi va divisa per la “ratio”). Tale parametro deve avere un valore di default pari a 1.

#Create quindi la classe Diff, che:
#
#-quando viene inizializzata accetti anche un parametro opzionale di nome ratio il cui valore di default sia 1
#
#- che abbia un metodo compute che prenda in input una lista di valori numerici e che ritorni in output la lista corrispondente alle loro differenze.
#
#Le eccezioni che devono essere alzate in caso di input non corretti o casi limite devono essere istanze di una specifica classe, ovvero “ExamException”, che dovete definire nel codice in esame.py come segue, senza modifica alcuna (copia-incollate le due righe):


    #class ExamException(Exception):

        #pass


#...e che poi userete come una normale eccezione, ad esempio:


    #raise ExamException(‘Errore, lista valori vuota’)

class ExamException(Exception):

    pass

class Diff():

    def __str__(self):
        return 'Difference'

    def __init__(self,ratio=1):
        
        #controllo se ratio va bene
        if ratio is None:
            raise ExamException("Non c'è nulla")
        
        if type(ratio) is str:
            raise ExamException('La ratio non è un numero')

        self.ratio = ratio

        if self.ratio <= 0:
            raise ExamException('La ratio ha un valore sbagliato')
        

    def compute(self,t):

        diff=[]

        i=0

        #controllo che sia una lista
        if not isinstance(t,list):
            raise ExamException('This is not a list, insert a list')

        #controllo che la lista non sia vuota
        elif t ==[]:
            raise ExamException('This list is empty, insert a valid list')

        elif len(t)<2:
            raise ExamException('The list is to short.')

        else:

            #controllo che il ratio non sia più grande degli elementi in diff
            for item in diff:
                if ratio > item in diff:
                    raise ExamException('Ratio is greater than list, please use small value.')
                    

            #controllo che in numbers ci siano solo numeri
            for item in t:
                if not isinstance(item,int) and not isinstance(item,float):
                    raise ExamException('Some elements are not numbers: list"{}"'.format(t))

            #faccio la differenza di tutti gli elementi

            #prendo elemento per elemento i dati
            for i, item in enumerate(t):
                #calcolo la differenza e li aggiungo ad un array
                if i == len(t) - 1:
                    break
                else:
                    diff.append((t[i + 1] - t[i]) / self.ratio)
        
        

            return diff


diff = Diff()


result = diff.compute([2,4,8,16])


print(result)





        

        
        

    
     
    