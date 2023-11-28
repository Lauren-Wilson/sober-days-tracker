from datetime import datetime

today = datetime.now()
today


sober = 'Oct 5 2018 2:00AM' 

# Function to convert string to datetime
def convert(date_time):
    format = '%b %d %Y %I:%M%p'
    datetime_str = datetime.strptime(date_time, format)
 
    return datetime_str
   

sober = convert(sober)

delta = today - sober
print(f'Difference is {delta.days} days')