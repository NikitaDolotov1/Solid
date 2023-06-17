#сдесь используется Принцип единственной ответственности (Single Responsibility Principle).
#Класс Human отвечает за пробуждение, класс Food отвечает за прием пищи, класс work отвечает за выполнение работы.


class Human:
    def __init__(self, name):
        self.name = name

    def wake_up(self):
        return f'{self.name} проснулся,'

class Food:
    def __init__(self, food):
        self.food = food

    def eat(self):
        return f'{h.name} поел {self.food},'

class work:

    def __init__(self, job):
        self.job = job

    def Job(self):
        return f'{h.name} пошел {self.job}'

h = Human ("Петя")
f = Food("Макароны")
w = work ("Работать")

print(f'{h.wake_up()} {f.eat()} {w.Job()}')








