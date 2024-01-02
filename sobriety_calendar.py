from datetime import datetime
from dateutil.relativedelta import relativedelta




today = datetime.now()
today

sober = '05-10-2018'
#sober = 'Oct 5 2018 2:00AM' 

# Function to convert string to datetime
def convert(date_time):
    #day month year format
    format = '%d-%m-%Y'
    datetime_str = datetime.strptime(date_time, format)

    time_difference = relativedelta(today, datetime_str)

    years_passed = time_difference.years
    months_passed = time_difference.months
    days_passed = time_difference.days

    delta = today - datetime_str
    days = delta.days

    return years_passed,months_passed, days_passed, days





    # format = '%b %d %Y %I:%M%p'
    # datetime_str = datetime.strptime(date_time, format)

    # delta = today - datetime_str
    


    # # Extract days, months, and years
    # days = delta.days
    # months = days // 30  # Assuming 30 days in a month for simplicity
    # years = days // 365

    # return years,months,days



    #     # Calculating years
    # years = delta // 365

    # # # Calculating months
    # months = (delta - years *365) // 30

    # # # Calculating days
    # days = (delta - years * 365 - months*30)
 
    
   

years, months, days_passed, days = convert(sober)
print(f'Today you are {years} years, {months} months, and {days_passed} days SOBER! Proud of you for {days} days!')