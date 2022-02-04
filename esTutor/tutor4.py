class Automotive():

    def __init__(self,name):
        self.name=name
        my_file = open(self.name, 'r')

        for line in my_file:
            elemnts = line.split(',')

            n_posti=elemnts[0]
            n_targhe=elemnts[1]
            marche_a=elemnts[3]
            modelli_a=elemnts[2]
        my_file.close()

    def __str__(self):
        my_file = open(self.name, 'r')

        #creo una lista vuoto
        Automotive = []
        #splitto sulla virgola
        if elemnts[0] != 'Posti':
            Automotive.append(elemnts)
        #chiudo il file
        my_file.close()
        #ritorno i valori
        return (Automotive)

    def parla(self):
        print('broom broom')

    def confronta(self):
        ele = lst[0]
        chk = True
      
    # Comparing each element with first item 
        for item in lst:
            if ele != item:
                chk = False
                break;
              
            if (chk == True):
                print("Equal")
            else:
                print("Not equal") 



    def casa_automo(self):
        my_file = open(self.name, 'r')
        #creo una lista vuoto
        marche = []

        
        if elemnts[0] != 'Posti':
            marche.append(marche_a)
        #chiudo il file
        my_file.close()
        #ritorno i valori
        return (marche)
        
    def modello(self):
        my_file = open(self.name, 'r')
        #creo una lista vuoto
        modelli = []
        
        if elemnts[0] != 'Posti':
            modelli.append(modelli_a)
        #chiudo il file
        my_file.close()
        #ritorno i valori
        return (modelli)

    def numero_posti(self):
        my_file = open(self.name, 'r')
        #creo una lista vuoto
        posti = []
        
        if elemnts[0] != 'Posti':
            posti.append(n_posti)
        #chiudo il file
        my_file.close()
        #ritorno i valori
        return (posti)

    def targa(self):
        my_file = open(self.name, 'r')
        #creo una lista vuoto
        targhe = []
        
        if elemnts[0] != 'Posti':
            targhe.append(n_targhe)
        #chiudo il file
        my_file.close()
        #ritorno i valori
        return (targhe)
    
my_file= Automotive('auto.csv')
casa= my_file.casa_automo()
print('Marca:',casa)
modello=my_file.modello()
print('Modello:',modello)
posti=my_file.numero_posti()
print('Numero posti:',posti)
targa=my_file.targa()
print('Targa:',targa)