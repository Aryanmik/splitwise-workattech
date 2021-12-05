import uuid


class Bill:

    def __init__(self, name, group_id, amount, payer_id):
        self.bill_id = f"BILL-{uuid.uuid1().hex[:6]}"
        self.name = name
        self.group_id = group_id
        self.amount = amount
        self.payer_id = payer_id