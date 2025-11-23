import dateutils
from datetime import datetime

def is_valid_run_mode(run_mode: str, msg: str) -> None:
    assert run_mode in ["R", "S"], msg

def is_not_null_nor_blank(value: str, msg: str) -> None:
    assert not (value is None or value.strip() == ""), msg

def is_null(value: str, msg: str) -> None:
    assert value is None, msg

def is_not_null(value: str, msg: str) -> None:
    assert value is not None, msg

def is_true(condition: bool, msg: str) -> None:
    assert condition, msg

def is_false(condition: bool, msg: str) -> None:
    assert not condition, msg

def is_int_between(val: int, lower_bound: int, upper_bound: int, msg: str) -> None:
    assert val >= lower_bound and val <= upper_bound, msg

def is_date_between(input_date: datetime, start_date: datetime, end_date: datetime, msg: str) -> None:
    assert start_date <= input_date <= end_date, msg
    
def is_valid_quarter(val: int, msg: str) -> None:
    is_int_between(val, dateutils.min_calendar_value, dateutils.quarters_in_year, msg)

def is_valid_month(val: int, msg: str) -> None:
    is_int_between(val, dateutils.min_calendar_value, dateutils.months_in_year, msg)

def is_equal_to(val1, val2, msg: str) -> None:
    assert val1 == val2, msg

def is_valid_year_quarter(year_quarter: str, msg: str = "invalid year quarter detected. investigate") -> None:
    assert year_quarter[4] == dateutils.year_quarter_sep and len(year_quarter) == 6, msg
