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
                    break
                else:
                    available_table = None
            if available_table is None:
                self.queue.put(guest)
                print(f'{guest.name} ожидает в очереди.')
            else:
                available_table.guest = guest
                print(f'{guest.name} сел(-а) за стол номер {available_table.number}')
                guest.start()

    def discuss_guests(self):
        while  self.queue.empty() is False or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if self.queue.empty() is False and table.guest is None:
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    next_guest.start()









tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()


