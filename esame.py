#Creare una classe "MovingAverange":
   #1)inizializzata con la lunghezza della finestra
   #2)che abbia un metodo compute:
       #2.1)imput lista valori serie
       #2.2)output lista valori media mobile
#effettuare controlli su:
   #1) imput
   #2)casi limite
#le eccezioni si devono chiamare così:
   #class ExamException(Exception):
        #pass
#...e che poi userete come una normale eccezione, ad esempio:
        #raise ExamException(‘Errore, lista valori vuota’)

#esempio di utilizzo:
    #moving_average = MovingAverage(2)


    #result = moving_average.compute([2,4,8,16])


    #print(result) # Deve stampare a schermo [3,6,12]

class ExamException(Exception):
    pass

     
class MovingAverage():

    def __str__(self):

        return ('MovingAverage')
    
    def __init__(self,window_size):

        #controllo che l'imput sia un intero
        if type(window_size) is not int:
            raise ExamException ('window_size must be int')

        #controllo che la finestra abbia almeno 1 elemento
        if not window_size>0:
            raise ExamException ('window_size must be >0') 

        self.window_size=window_size


    def compute(self,numbers):

        self.numbers=numbers

        moving_avaranges=[]

        i=0

        #controllo che sia una lista
        if not isinstance(numbers,list):
            raise ExamException('This is not a list, insert a list')

        #controllo che la lista non sia vuota
        elif numbers ==[]:
            raise ExamException('This list is empty, insert a valid list')
        
        #se ho superato queste condizioni allora posso procedere
        else:

            #controllo che window_size!>numbers
            if self.window_size > len(numbers):
                raise ExamException('Window is greater than list. window_size is "{}" and numbers is "{}", please use small value.'.format(window_size,len(numbers)))
            
            #controllo che in numbers ci siano solo numeri
            for item in numbers:
                if not isinstance(item,int) and not isinstance(item,float):
                    raise ExamException('Some elements are not numbers: list"{}"'.format(numbers))

            #faccio la media degli elementi e la assegno alla lista vuota poi faccio return
            while i< len(numbers)-self.window_size+1:

                window=numbers[i:i+self.window_size]
                window_avarage=int((sum(window)/self.window_size)) 
                moving_avaranges.append(window_avarage)
                i=i+1

            return moving_avaranges


try:
    w_s=2
    
    moving_average = MovingAverage(w_s)

    l=[2,4,8,16]

    result = moving_average.compute(l)

    print('The moving averange of "{}" is:'.format(l)) 

    print(result)

except TypeError:
    raise ExamException('No space allow or words allow in window_size ')


   
                
                    
                    
                

            
            

        
        

        