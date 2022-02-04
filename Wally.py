import random

class Automa():

    def __init__(self):

        self.biancheria=None
        self.calzini=None
        self.maglia=None
        self.pantaloni=None
        self.calzatura=None
        self.vestito=False

    def __str__(self):

        return('Automa\n {}\n {}\n {}\n {}\n {}'.format(self.biancheria,self.calzini,self.maglia,self.pantaloni,self.calzatura))

    def indossare_biancheria(self):
        self.biancheria=True
        return 1

    def indossare_calzini(self):
        if self.biancheria:
            self.calzini=True
            return 1
        else:
            return 0

    def indossare_maglia(self):
        if self.calzini:
            self.maglia=True
            return 1
        else:
            return 0

    def indossare_pantaloni(self):
        if self.maglia:
            self.pantaloni=True
            return 1
        else:
            return 0

    def indossare_calzatura(self):
        if self.pantaloni:
            self.calzatura=True
            self.vestito=True
            return 1
        else:
            return 0
    
    

def vestiti(automa,capo):
    all_attributes= ['biancheria','calzini','maglia','pantaloni','calzatura']

    for i, attribut in enumerate(all_attributes):
        if capo == attribut:
            if i == 0:
                return automa.indossare_biancheria()
            if i == 1:
                return automa.indossare_calzini()
            if i == 2:
                return automa.indossare_maglia()
            if i == 3:
                return automa.indossare_pantaloni()
            if i ==4:
                return automa.indossare_calzatura()
                

capi=['biancheria','calzini','maglia','pantaloni','calzatura']
vestito=False
Wally=Automa()

while not vestito:
    capo=random.choice(capi)
    vestiti(Wally,capo)
    print(Wally)
    vestito=Wally.vestito

print('Wally è pronto per uscire')
print(Wally)
        