from constant import SPLITTYPE
from service.splitwise_service import SplitWiseService

if __name__ == "__main__":
    split_wise = SplitWiseService()

    user1 = split_wise.create_user(name="Aryan", phone_number="123")
    user2 = split_wise.create_user(name="Suresh", phone_number="1234")
    user3 = split_wise.create_user(name="Ramesh", phone_number="12345")

    weekend_party_group = split_wise.create_group(group_name="weekend_party")

    add_users_in_weekend_party_group = split_wise.add_user_in_group(group_id=weekend_party_group.id,
                                                                    users_ids=[user1.id, user2.id, user3.id])

    bill_1 = split_wise.create_bill(bill_name="Alcohol", group_id=weekend_party_group.id, amount=1000,
                                    split_type=SPLITTYPE.EQUAL, payer_id=user1.id, users=None)

    bill_2 = split_wise.create_bill(bill_name="Food", group_id=weekend_party_group.id, amount=None,
                                    split_type=SPLITTYPE.EXACT, payer_id=user1.id,
                                    users={user2.id : 100, user3.id : 200})

    split_wise.show_balance_of_user(user2.id)
    split_wise.show_balance_of_group(weekend_party_group.id)
