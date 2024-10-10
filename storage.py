import json
from event import Event


class Storage:
    FILE_PATH = "calendar_date.json"

    @staticmethod
    def save_events(events):
        with open(Storage.FILE_PATH, 'w') as file:
            json.dump([event.to_dict() for event in events], file)

    @staticmethod
    def load_events():
        try:
            with open(Storage.FILE_PATH, 'r') as file:
                events = json.load(file)
                return [Event.from_dict(event) for event in events]
        except FileNotFoundError:
            return []