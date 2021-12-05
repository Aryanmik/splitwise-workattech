import math

from constant import SPLITTYPE
from database.bills import BillsDb
from database.groups import GroupsDb
from database.users import UsersDb
from models.bill import Bill
from models.group import Group
from models.users import User


class SplitWiseService:

    def __init__(self):
        self.bills = BillsDb()
        self.groups = GroupsDb()
        self.users = UsersDb()


    def create_user(self, name , phone_number):
        user = User(name, phone_number)
        self.users.save(user)
        return user

    def create_group(self, group_name):
        group = Group(group_name)
        self.groups.save(group)
        return group

    def add_user_in_group(self, group_id, users_ids):
        group = self.groups.get(group_id)
        users = [self.users.get(user_id) for user_id in users_ids]
        group.add_user_in_group(users)
        return group


    def create_bill(self, payer_id, bill_name , group_id, amount , split_type, users):
        bill = Bill(bill_name, amount, group_id, payer_id)

        payer = self.users.get(payer_id)
        group = self.groups.get(group_id)

        if split_type == SPLITTYPE.EQUAL:
            split_amount = round((amount/len(group.users)),2)
            for user in group.users:
                if user.id != payer_id:
                    user.owes[payer_id].append(split_amount)
                    payer.get_paid[user.id].append(split_amount)
        elif split_type == SPLITTYPE.EXACT:
            for user_id, amount in users.items():
                user = self.users.get(user_id)
                user.owes[payer_id].append(amount)
                payer.get_paid[user.id].append(amount)


        bill = self.bills.save(bill)
        group.attach_bill(bill.bill_id)
        return bill

    def show_balance_of_user(self, user_id):
        user = self.users.get(user_id)
        for user_id, amounts in user.owes.items():
            print(f"{user.name} owes {self.users.get(user_id).name} : {sum(amounts)}")


    def show_balance_of_group(self, group_id):
        group = self.groups.get(group_id)
        for user in group.users:
            for user_id, amounts in user.owes.items():
                print(f"{user.name} owes {self.users.get(user_id).name} : {sum(amounts)}")