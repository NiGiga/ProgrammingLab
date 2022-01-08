#creo la classe
class IncrementModel():

  def __init__(self,data):

    self.data = data

  #creo la funzione per prevedere l' andamento della distribuzione
  def predict(self):

    precedente = None
    n = len(self.data)
    
    #controllo se la data è una stringa
    

    if isinstance(self.data,list):

      print('la data è una lista')

    else:
      return('la data non è una lista')
      

    if (n <= 2):

      print('non posso fare la previsione perchè data ha troppi pochi dati \n')
      
      return 'inserire una lista con più di 2 elementi'

    #altrimenti
    else:

      for item in self.data:
        
        if precedente is not None:

          diff = item - precedente
          base = item

        else:
          precedente = item

    return base+(diff/(n-1))

l = [50,52,60]
previu = IncrementModel(l)
print(previu.predict())
