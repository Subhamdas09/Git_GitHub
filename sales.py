class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, odr2):
        return self.price > odr2.price

Order1 = Order("chai", "20")
Order2 = Order("samosha", "30")

print(Order1>Order2)