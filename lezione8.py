#creare un modello ricordandosi di creare le condizioni

#==================================

#Classe IncrementalModel

#==================================

class IncrementalModel():

    def __init__(self,data):

        self.data=data

    #creo la funzione predict

    def predict(self):

        n_meno_uno = None
        n = len(self.data)

        #controllo che data sia una lista e che contenga #almeno 2 valori

        if isinstance (self.data,list):

            print('->')
        else:

            return ('Data is not a list.')

        if (n<2):

            print('The number of variables is less than 2, predict impossible. Pleas insert more variables!')
        
        else:

            #calcolo la predizione

            for item in self.data:

                if n_meno_uno is not None:

                    diff= item - n_meno_uno
                    t0 = item
                else:
                    n_meno_uno=item
                    
        
        return t0 + (diff/(n-1))
                    
#==================================

#Corpo del programma

#==================================
            
l = [50,52,60]
previsione = IncrementalModel(l)
print('############################')
print('La previsione di vendita è:')
print(previsione.predict())
print('############################')
print('Registrando un incremendto di:')
print(previsione.predict()-l[-1])
print('############################')
            

        



        