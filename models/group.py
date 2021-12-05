import uuid
from typing import List

from models.users import User


class Group:

    def __init__(self, name, users : List[User] = None):
        self.id = f"GID-{uuid.uuid1().hex[:6]}"
        self.name = name
        self.users = users
        self.bill_ids = []

    def add_user_in_group(self, users):
        self.users = users

    def attach_bill(self, bill_id):
        self.bill_ids.append(bill_id)