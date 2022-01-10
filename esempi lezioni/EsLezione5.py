my_var = 'Ciao'
#inserisco il cosstrutto try-exept
try:
    my_var = float(my_var)
except ValueError:
    print('Non posso convertire la variabile "my_var"')
    print('Ed ho avuto un errore di Valore. "my_var" valeva "{}"'.format(my_var))
except TypeError:
    print('Non posso convertire la variabile "my_var"')
    print('Ed ho avuto un error di TIPO. "my_var"valeva "{}"'.format(float(my_var)))
except Exception as e:
    print('Non posso convertire la variabile "my_var"')
    print('Ed ho avuto un errore generico "{}"'.format(e))