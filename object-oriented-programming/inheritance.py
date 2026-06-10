class Cars:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def loading_data(self):
        print("Loading Data...")


class Mercedes(Cars):
    def show(self):
        super().loading_data()      # Calling parent class method
        return f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}"


m = Mercedes("Mercedes", "GLS", "10000000")
print(m.show())