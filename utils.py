import datetime

import calendar
from event import Event


def parse_date(date: str) -> datetime.datetime:
    return datetime.datetime.strptime(date, "%Y-%m-%d")


def get_events_for_period(events: list[Event], start_date: datetime, end_date: datetime):
    return [event for event in events if start_date <= parse_date(event.date) <= end_date]


def get_week_range(date: datetime):
    weekday = date.weekday()
    if weekday == 0:
        start_date = date
    else:
        start_date = date - datetime.timedelta(days=weekday)
    end_date = start_date + datetime.timedelta(days=6)
    return start_date, end_date

def get_month_range(date: datetime):
    start_date = datetime.datetime(date.year, date.month, 1)
    end_date = start_date + datetime.timedelta(days=calendar.monthrange(date.year, date.month)[1])
    return start_date, end_date
