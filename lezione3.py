#creo una variabile vuota
values = []
#apro il file
my_file = open('shampoo_sales.txt', 'r')
#eseguo lo split
for line in my_file:
  elements = line.split(',')
#non processo l'intestazione
  if elements[0] != 'Date':
    
#setto i valori 
    date = elements[0]
    value = elements[1]
#aggiungo questo valore
    values.append(float(value))
#sommo i valori
sum(values)
#stampo i valori
print(sum(values))
#chiudo il file
my_file.close()














   

     


