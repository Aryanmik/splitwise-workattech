import uuid

from collections import defaultdict


class User:

    def __init__(self, name, phone_number):
        self.id = f"UID-{uuid.uuid1().hex[:6]}"
        self.name = name
        self.phone_number = phone_number
        self.owes = defaultdict(list)
        self.get_paid = defaultdict(list)
