from random import randrange


class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, element):
        self.array.append(element)

    def dequeue(self):
        if not self.array:
            return None
        else:
            return self.array.pop(0)

    def __str__(self):
        new_q = Queue()
        for i in range(len(self.array)):
            new_q.enqueue(str(self.array[i]))
        return ", ".join(new_q.array)

    def __add__(self, other):
        new_q = Queue()
        for elem in self.array:
            new_q.enqueue(elem)
        new_q.enqueue(other)
        return new_q

    def __iadd__(self, other):
        self.enqueue(other)
        return self

    def __neg__(self):
        return self.dequeue()

    def __len__(self):
        return len(self.array)


class Bank:
    def __init__(self, n):
        cashes = []
        for i in range(n):
            cashes.append(Queue())
        self.cashes = cashes

    def customer_enters(self, full_name):
        x = randrange(len(self.cashes))
        self.cashes[x].enqueue(full_name)
        print(f"Customer {full_name} is in the queue of cash {x} to be served")

    def customer_served(self):
        not_empty_cash_desks = [i for i in range(len(self.cashes)) if len(self.cashes[i]) > 0]

        if len(not_empty_cash_desks) > 0:
            cash_desk = not_empty_cash_desks[randrange(len(not_empty_cash_desks))]
            customer = - self.cashes[cash_desk]
            print(f"Customer {customer} served successfully by cash {cash_desk}!")
        else:
            print("No customer")

    def __str__(self):
        string = "="*20+"\n"
        for i in range(len(self.cashes)):
            string += f"Cash {i}: {str(self.cashes[i])}\n"
        string += "=" * 20 + "\n"
        return string


b1 = Bank(3)
for i in range(1,101):
    x = randrange(1, 11)    #etsi apla vazoume kai pithanothtes sto programma
    if 0 < x < 4:
        b1.customer_served()
    else:
        b1.customer_enters(str(i))
    if i % 10 == 0:
        print(b1)






