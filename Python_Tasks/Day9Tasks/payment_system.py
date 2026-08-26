#11. Payment System (Runtime Polymorphism)

class Payment:

    def process_payment(self):
        print("Processing Payment...")


class CreditCard(Payment):

    def process_payment(self):
        print("Payment made using Credit Card")


class UPI(Payment):

    def process_payment(self):
        print("Payment made using UPI")


class NetBanking(Payment):

    def process_payment(self):
        print("Payment made using Net Banking")


payment1 = CreditCard()
payment2 = UPI()
payment3 = NetBanking()

payment1.process_payment()
payment2.process_payment()
payment3.process_payment()