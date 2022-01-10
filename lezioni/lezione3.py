#scrivere uno script c he sommi tutti i valori di vendita di shampoo

def funzione_somma(my_file):

    #creo una lista vuota
    values=[]
   

    #eseguo lo split

    for line in my_file:

        elements= line.split(',')

        #se non processo l'intestazione

        if (elements[0]!='Date'):

            
            Value= elements[1]

            #aggiungo value a values

            values.append(float(Value))
        
    my_file.close()
    return (sum(values))
    
#corpo
my_file= open('shampoo_sales.csv','r')
print(funzione_somma(my_file))














   

     


