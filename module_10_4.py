from threading import Thread
from random import randint
import queue
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        expectation = randint(3, 10)
        sleep(expectation)

class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        available_table = None
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    available_table = table
                else:
                    available_table = None
            if available_table is None:
                self.queue.put(guest)
                print(f'{guest.name} ожидает в очереди.')
            else:
                available_table.guest = guest
                print(f'{guest.name} сел(-а) за стол номер {available_table.number}')
                guest.start()

    # def discuss_guests(self):








tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
# cafe.discuss_guests()

