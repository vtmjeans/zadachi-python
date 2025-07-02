from datetime import datetime, timedelta

def date_in_future(integer):
    now = datetime.now()
    if isinstance(integer, int):
        result_date = now + timedelta(days=integer)
    else:
        result_date = now
    return result_date.strftime('%d-%m-%Y %H:%M:%S')
print(date_in_future(2))         
print(date_in_future(0))         
print(date_in_future(-4))       