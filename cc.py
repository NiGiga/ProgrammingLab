
#import datetime
from datetime import datetime
 
# consider the datetime string in dd/mm/yyyy
# hh:mm:ss format
date = ["25/05/2021 02:35:15","25/05/2021 02:35:15"]
 
# convert string datetime to  dd/mm/yyyy hh:mm:ss
# format
datetime_date = datetime.strptime(date, "%d/%m/%Y %H:%M:%S")
print(datetime_date)