from random import randrange

class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.served_cnt = 0

    def __str__(self):
        return str(self.name)


class Waiter(Person):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def serve(self, customer_number, barista):
        print(f"{self.name} gave the order of {customer_number} customers to barista {barista.name}")
        barista.prepare(customer_number)
        self.served_cnt += customer_number


class Barista(Person):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def prepare(self, customers):
        print(f"Barista {self.name} is preparing the drinks for {customers} people")
        self.served_cnt += customers


class Owner(Waiter, Barista):
    def __init__(self, name, salary):
        super().__init__(name, salary)


o = Owner("Levantofski", 1000)
w1 = Waiter("Papoutsou", 300)
w2 = Waiter("Alex", 300)
b = Barista("Geegees", 400)
waiters = [w1, w2, o]
baristas = [b, o]
for i in range(10):
    waiters[randrange(3)].serve(randrange(1,6), baristas[randrange(2)])
print("\n--------------------------------\n")
for i in range(2):
    print(f"{waiters[i]} served {waiters[i].served_cnt} people")
for i in range(2):
    print(f"{baristas[i]} served {baristas[i].served_cnt} people")










