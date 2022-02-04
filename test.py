import random

class Automa():
    
    

    def __init__(self):

        self.biancheria = None
        self.calzini = None
        self.maglia = None
        self.pantaloni = None
        self.calzatura = None
        self.vestito = False

    def __str__(self):

        return('Automa\n {}\n {}\n {}\n {}\n {}'.format(self.biancheria, self.calzini, self.maglia, self.pantaloni, self.calzatura))

    def fun_biancheria(self):
        self.biancheria = True
        return 1
    
    def fun_calzini(self):
        if self.biancheria:
            self.calzini = True
            return 1
        else:
            return 0
    
    def fun_maglia(self):
        if self.calzini:
            self.maglia = True
            return 1
        else:
            return 0
    
    def fun_pantaloni(self):
        if self.maglia:
            self.pantaloni = True
            return 1
        else:
            return 0
    
    def fun_calzatura(self):
        if self.pantaloni:
            self.calzatura = True
            self.vestito = True
            return 1
        else:
            return 0

def esegui(automa, capo):

    all_attributes = ['biancheria', 'calzini', 'maglia', 'pantaloni', 'calzatura']

    for i, attributo in enumerate(all_attributes):
        if capo == attributo:
            if i == 0:
                return automa.fun_biancheria()
            if i == 1:
                return automa.fun_calzini()
            if i == 2:
                return automa.fun_maglia()
            if i == 3:
                return automa.fun_pantaloni()
            if i == 4:
                return automa.fun_calzatura()


capi_vastiario = ['biancheria', 'calzini', 'maglia', 'pantaloni', 'calzatura']
vestito = False
rob_cop = Automa()

while not vestito:
    
    capo = random.choice(capi_vastiario)
    esegui(rob_cop, capo)
    print(rob_cop)
    vestito = rob_cop.vestito

print('-------')
print(rob_cop)
