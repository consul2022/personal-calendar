import datetime

from event import Event
from storage import Storage
from utils import parse_date, get_events_for_period, get_week_range, get_month_range


class Calendar:
    def __init__(self):
        self.events = Storage.load_events()

    def add_event(self, date: str, time: str, category: str, title: str, description: str):
        new_event = Event(date, time, category, title, description)
        self.events.append(new_event)
        Storage.save_events(self.events)
        print("Событие добавленно")

    def edit_event(self, event_id: int, date: str, time: str, category: str, title: str, description: str):
        if 0 <= event_id < len(self.events):
            self.events[event_id].update(date, time, category, title, description)
            Storage.save_events(self.events)
            print("Событие изменено")
        else:
            print("События с таким ID не найдено")

    def delete_event(self, event_id: int):
        if 0 <= event_id < len(self.events):
            del self.events[event_id]
            Storage.save_events(self.events)
            print("Событие удалено")
        else:
            print("События с таким ID не найдено")

    def view_event(self, event_id: int):
        if 0 <= event_id < len(self.events):
            print(self.events[event_id])
            return self.events[event_id]
        else:
            print("События с таким ID не найдено")


    def search_event(self, keyword: str):
        result = []
        for event in self.events:
            if keyword.lower() in event.category.lower() or keyword.lower() in event.description.lower() or keyword == event.date:
                result.append(event)
        if result:
            print("Найденные события:")
            for event in result:
                print(event)
        return result

    def view_event_by_day(self, date: str):
        selected_date = parse_date(date)
        events = get_events_for_period(self.events, selected_date, selected_date)
        if events:
            print(f"События на {date}:")
            for event in events:
                print(event)
        else:
            print("На этот день нет событий")
        return events

    def view_events_by_week(self, start_date: str, end_date: str):
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)
        events = get_events_for_period(self.events, start_date, end_date)
        if events:
            print(f"События в неделю с {start_date.strftime('%d.%m.%Y')} по {end_date.strftime('%d.%m.%Y')}:")
            for event in events:
                print(event)
        else:
            print("На эту неделю нет событий")
        return events

    def view_events_by_month(self, month:int, year:int):
        selected_date = datetime.datetime(year, month, 1)
        start_date, end_date = get_month_range(selected_date)
        events = get_events_for_period(self.events, start_date, end_date)
        if events:
            print(f"События в месяц {selected_date.strftime('%B %Y')}:")
            for event in events:
                print(event)
        else:
            print("На этот месяц нет событий")
        return events


    def view_events_by_year(self, year:int):
        events = [event for event in self.events if event.date[:4] == str(year)]
        if events:
            print(f"События в {year} году:")
            for event in events:
                print(event)
        else:
            print(f"На {year} году нет событий")
        return events


    def clear_events(self):
        self.events = []
        Storage.save_events(self.events)
        print("События удалены")