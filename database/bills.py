class BillsDb:
    bills = {}

    def get(self, bill_id):
        return self.bills.get(bill_id)

    def save(self, bill):
        self.bills[bill.bill_id] = bill
        return bill
