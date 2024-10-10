class Event:
    def __init__(self, date: str, time: str, category: str, title: str, description: str):
        self.date = date
        self.time = time
        self.category = category
        self.title = title
        self.description = description

    def __str__(self):
        return f"{self.title} ({self.category}): {self.date} {self.time}, {self.description}"

    def update(self, date: str, time: str, category: str, title: str, description: str):
        self.date = date
        self.time = time
        self.category = category
        self.title = title
        self.description = description



    def to_dict(self):
        return {
            "date": self.date,
            "time": self.time,
            "category": self.category,
            "title": self.title,
            "description": self.description
        }

    @staticmethod
    def from_dict(data):
        return Event(**data)





