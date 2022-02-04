from datetime import datetime 

def lettura_date():
    my_file = open('shampoo_sales.csv', 'r')
    dates = []
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            data = datetime.strptime(elements[0], '%d-%m-%Y')
            dates.append(data)
    my_file.close()
    return dates

date_vendite = lettura_date()
for data in date_vendite:
    print(data.strftime('%d-%m-%Y'))