#implementare una funzione che ritorni le date delle vendite del file shampoo_sales.csv
#si dovra usare un modulo per convertire le date:

#from datetime import datetime
#....
#my_date=datetime.strptime(elements[0],'%d-%m-%Y')

from datetime import datetime 

def lettura_date(my_file):
    
    dates = []
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            data = datetime.strptime(elements[0], '%d-%m-%Y')
            dates.append(data)
    my_file.close()
    return dates


my_file = open('shampoo_sales.csv', 'r')
date_vendite = lettura_date(my_file)
for data in date_vendite:
    print(data.strftime('%d-%m-%Y'))

