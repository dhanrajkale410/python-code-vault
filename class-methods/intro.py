class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))  # Creates a new Person instance

p = Person.from_string("Alice-30")
print(p.name, p.age)  # Alice 30