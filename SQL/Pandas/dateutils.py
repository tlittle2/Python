from pandas import DataFrame, DateOffset, Series
from datetime import datetime
import pdutils
from numpy import sign

months_in_year: int = 12
quarters_in_year: int = 4
months_in_quarter: int = 3
min_calendar_value : int = 1
year_quarter_sep: str = "Q"

col_date = "date"
col_year_quarter = "year_quarter"

def __is_validate_year_quarter(year_quarter) -> bool:
    return year_quarter[4] == year_quarter_sep and len(year_quarter) == 6

def format_year_quarter(year: int, month: int) -> str:
    return "{}{}{}".format(year, year_quarter_sep, month)

def get_quarter(month: int) -> int:
    assert pdutils.is_between(month, min_calendar_value, months_in_year), "invalid month provided. investigate"
    quarter = (month - min_calendar_value) // months_in_quarter + min_calendar_value
    assert pdutils.is_between(quarter, min_calendar_value, quarters_in_year), "invalid quarter returned. investigate"
    return quarter

def get_year_quarter(date: datetime) -> str:
    return format_year_quarter(date.year, get_quarter(date.month))

def get_new_year_quarter(year_quarter: str, num_of_quarters: int) -> str:
    temp_date = get_min_date_for_year_quarter(year_quarter) + DateOffset(months=num_of_quarters * months_in_quarter)
    return get_year_quarter(temp_date)

def get_year_from_year_quarter(year_quarter: str) -> int:
    assert __is_validate_year_quarter(year_quarter)
    return int(year_quarter[0:4])

def get_quarter_from_year_quarter(year_quarter: str) -> int:
    assert __is_validate_year_quarter(year_quarter)
    return int(year_quarter[5])

#====================================================================================================
def get_min_date_for_year_quarter(year_quarter: str) -> datetime:
    year: int = get_year_from_year_quarter(year_quarter)
    quarter: int = get_quarter_from_year_quarter(year_quarter)
    month: int = (quarter - min_calendar_value) * months_in_quarter + min_calendar_value

    return datetime(year, month, min_calendar_value)

def get_min_date_for_quarter(date: datetime) -> datetime:
    return get_min_date_for_year_quarter(get_year_quarter(date))

def get_max_date_for_year_quarter(year_quarter: str) -> datetime:
    min_date = get_min_date_for_year_quarter(year_quarter)

    max_date = (min_date + DateOffset(months=months_in_quarter)) - DateOffset(days=min_calendar_value)

    return max_date

def get_max_date_for_quarter(date: datetime) -> datetime:
    return get_max_date_for_year_quarter(get_year_quarter(date))

#====================================================================================================

def __is_quarter(year_quarter: str, q_num: int) -> bool:
    assert pdutils.is_between(q_num, min_calendar_value, quarters_in_year), "invalid quarter provided. investigate"
    return get_quarter_from_year_quarter(year_quarter) == q_num

def is_quarter1_yq(year_quarter: str) -> bool:
    return __is_quarter(year_quarter, 1)

def is_quarter1_dt(date: datetime) -> bool:
    return is_quarter1_yq(get_year_quarter(date))

def is_quarter2_yq(year_quarter: str) -> bool:
    return __is_quarter(year_quarter, 2)

def is_quarter2_dt(date: datetime) -> bool:
    return is_quarter2_yq(get_year_quarter(date))

def is_quarter3_yq(year_quarter: str) -> bool:
    return __is_quarter(year_quarter, 3)

def is_quarter3_dt(date: datetime) -> bool:
    return is_quarter3_yq(get_year_quarter(date))

def is_quarter4_yq(year_quarter: str) -> bool:
    return __is_quarter(year_quarter, quarters_in_year)

def is_quarter4_dt(date: datetime) -> bool:
    return is_quarter4_yq(get_year_quarter(date))


#====================================================================================================


def get_days(start_date: datetime, num_of_days: int)-> DataFrame:
    s = Series([start_date + DateOffset(days = sign(num_of_days) * i) for i in range(abs(num_of_days))] )
    return DataFrame({col_date: s})

def get_dates(start_date: datetime, end_date: datetime)-> DataFrame:
    days = (end_date - start_date).days
    return get_days(start_date, days)

def get_year_quarters(start_quarter: str, num_of_quarters: int)-> DataFrame:
    assert __is_validate_year_quarter(start_quarter), "invalid starting year quarter provided. please investigate"

    s = Series([get_new_year_quarter(start_quarter, sign(num_of_quarters) * i) for i in range(abs(num_of_quarters))] )

    return DataFrame({col_year_quarter: s})
