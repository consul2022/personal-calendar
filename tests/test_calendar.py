import pytest
from calendar_events import Calendar


@pytest.fixture
def calendar():
    calendar = Calendar()
    calendar.clear_events()
    return calendar


def test_add_event(calendar):
    calendar.add_event("2022-01-01", "10:00", "Заработка", "Работа вчера", "Запланирована")
    assert len(calendar.events) == 1
    assert calendar.events[0].date == "2022-01-01"
    assert calendar.events[0].title == "Работа вчера"
    assert calendar.events[0].time == "10:00"
    assert calendar.events[0].category == "Заработка"
    assert calendar.events[0].description == "Запланирована"



def test_edit_event(calendar):
    calendar.add_event("2022-01-01", "10:00", "Заработка", "Работа вчера", "Запланирована")
    calendar.edit_event(0, "2022-01-01", "12:00", "Обед", "Работа вчера", "Изменено")
    assert calendar.events[0].time == "12:00"
    assert calendar.events[0].category == "Обед"
    assert calendar.events[0].title == "Работа вчера"
    assert calendar.events[0].description == "Изменено"


def test_delete_event(calendar):
    calendar.add_event("2022-01-01", "10:00", "Заработка", "Работа вчера", "Запланирована")
    calendar.delete_event(0)
    assert len(calendar.events) == 0


def test_view_event_by_day(calendar):
    calendar.add_event("2022-01-01", "10:00", "Заработка", "Работа вчера", "Запланирована")
    calendar.add_event("2022-01-02", "11:00", "Учеба", "Уроки", "Запланирована")
    events = calendar.view_event_by_day("2022-01-01")
    assert len(events) == 1
    assert events[0].title == "Работа вчера"


def test_view_event_by_week(calendar):
    calendar.add_event("2022-01-01", "10:00", "Заработка", "Работа вчера", "Запланирована")
    calendar.add_event("2022-01-02", "11:00", "Учеба", "Уроки", "Запланирована")
    events = calendar.view_events_by_week("2022-01-01","2022-01-07")
    assert len(events) == 2
    assert events[0].title == "Работа вчера"
    assert events[1].title == "Уроки"



def test_view_by_month(calendar):
    calendar.add_event("2022-01-01", "10:00", "Заработка", "Работа вчера", "Запланирована")
    calendar.add_event("2022-01-02", "11:00", "Учеба", "Уроки", "Запланирована")
    events = calendar.view_events_by_month(1,2022)
    assert len(events) == 2
    assert events[0].title == "Работа вчера"
    assert events[1].title == "Уроки"


def test_search_event(calendar):
    calendar.add_event("2022-01-01", "10:00", "Заработка", "Стройка", "Работа вчера")
    calendar.add_event("2022-01-02", "11:00", "Работа и учеба", "Уроки", "Запланирована")
    events = calendar.search_event("работа")
    assert len(events) == 2
    assert events[0].title == "Стройка"
    assert events[1].title == "Уроки"

def test_view_event(calendar):
    calendar.add_event("2022-01-01", "10:00", "Заработка", "Работа вчера", "Запланирована")
    calendar.view_event(0)
    assert len(calendar.events) == 1
    assert calendar.events[0].title == "Работа вчера"





