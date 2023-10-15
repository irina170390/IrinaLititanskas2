from datetime import datetime


class Order:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def get_timestamp(self):
        return self.timestamp

    def __str__(self):
        formatted_time = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        items_list = ", ".join(item.get_name() for item in self.items)
        return f"Order placed at {formatted_time}\n{items_list}"