#importo il random
import random
 #creo l'oggetto
class Person():
    #inizializzo
    def __init__(self,name,surname):
        #setto name e surname
        self.name    = name
        self.surname = surname
    #oggetto persona
    def __str__(self):
        return 'Persona {} {}'.format(self.name, self.surname)
    #creo funzione randomica
    def say_hi(self):
        #imposto random rang
        random_num = random.randint(0,2)
        #creo le variabili
        if random_num == 0:
            print('Hello, I am {} {}'.format(self.name, self.surname))
        elif random_num == 1:
            print('Hei there, I am {} {}'.format(self.name, self.surname))
        elif random_num == 2:
            print('Yoh Broh, {} there'.format(self.name))
 
#estendo l'oggetto
class Student(Person):
    #sovvrascrivo l'oggetto persona per dare un titolo (studente)
    def __str__(self):
        return 'studente {} {}'.format(self.name, self.surname)
     #richiamo la funzione originale
    def original_say_hi(self):
        super().say_hi()
#estendo l'oggetto
class Professor(Person):
    #sovvrascrivo l'oggetto persona per dare un titolo(Prof.)
    def __str__(self):
        return 'Prof. {} {}'.format(self.name, self.surname)
    #sovvrascrivo la funzione per dare un sauto più consono al professore
    def say_hi(self):
        print('Hello, I am Professor {} {}'.format(self.name, self.surname))
    #richiamo l'originale
    def original_say_hi(self):
        super().say_hi()

#stampo a schermo person
print('________________________________________')

person = Person('Nicola','Giga')
print(person)
person.say_hi()

#stampo a schermo Professor
print('________________________________________')

prof = Professor('Don','Matteo')
print(prof)
prof.say_hi()
prof.original_say_hi()

#stampo a schermo student
print('________________________________________')

studente = Student('Giovanni','Muciaccia')
print(studente)
studente.original_say_hi()

print('________________________________________')

