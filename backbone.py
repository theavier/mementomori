import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta
from loguru import logger

#max_age = 85
#birthday = "1983-05-06"

logger.add(sys.stderr, level="DEBUG")

def get_result(input_form):
    logger.debug(f'Starting')
    _birthday, _max_age = input_form["birthdate"], input_form["max_age"]
    logger.info(f'birthdate: {_birthday}, max {_max_age}')
    if not validate_birthday(_birthday):
        return "Wrong format"
    if _birthday and _max_age:
        days_left = get_days_left(_birthday, _max_age)
        if days_left:
            return f"You got {days_left} days left"
        else:
            return "Something went wrong"
    else:
        return "missing values"
    return "myresult"


def validate_birthday(_bday):
    logger.debug('Starting')
    try:
        bday_date = datetime.strptime(_bday, "%Y-%m-%d")
        return True
    except:
        return False

def get_days_left(bday, max_age):
    logger.debug(f'Starting. Values bday {bday} ({type(bday)}), max {max_age} ({type(max_age)})')
    bday_date = datetime.strptime(bday, "%Y-%m-%d")
    end_day = bday_date + relativedelta(years=int(max_age))
    this_today = datetime.today()
    days_left = (this_today - end_day).days * -1
    return days_left

#my_days = get_days_left(birthday, max_age)
#print(f'Memento Mori')
#print(f'Your age: {age}, your expected age {max_age}')
#print(f'your birthday {bday_date}, endday {end_day}')
#print(f'you have {my_days} days left.')