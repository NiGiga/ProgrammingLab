def even_items(iterable):

    return [v for i, v in enumerate(iterable, start=1) if not i % 2]

#invece che

def even_items(iterable):
...     """Return items from ``iterable`` when their index is even."""
...     values = []
...     for index, value in enumerate(iterable, start=1):
...         if not index % 2:
...             values.append(value)
...     return values
...
           numerical_row=[] 

 return [n_r for i, n_r in enumerate(string_row) if i==0 else try n_r for i, n_r in enumerate(float(string_row)) except Exception as e print('Errore')]

                if i == 0:

                    numerical_row.append(element)
                
                #converto tutti i valori a float ma se non ci riesco rompo il ciclo e stamo l'Errore

                else:
                    try:

                        numerical_row.append(float(element))
                    
                    except Exception as e:

                        print('Errore in conversione del valore "{}" a float. L errore è:{}'.format(element,e))
                        break
            #ora controllo per lunghezza e se coincidono stampo la lista

            if len(numerical_row)==len(string_row):

                numerical_data.append(numerical_row)
        
        return numerical_data