from datetime import datetime


class Note:
    def __init__(self, id, title, content, timestamp=None):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp,
        }

    @staticmethod
    def from_dict(data):
        return Note(
            id=data["id"],
            title=data["title"],
            content=data["content"],
            timestamp=data["timestamp"],
        )


class Task:
    def __init__(
        self, id, title, description, done=False, priority="Средний", due_date=None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "priority": self.priority,
            "due_date": self.due_date,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            done=data["done"],
            priority=data["priority"],
            due_date=data["due_date"],
        )


class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            id=data["id"], name=data["name"], phone=data["phone"], email=data["email"]
        )


class FinanceRecord:
    def __init__(self, id, amount, category, date, description):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }

    @staticmethod
    def from_dict(data):
        return FinanceRecord(
            id=data["id"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            description=data["description"],
        )
