import random

class Human:
    def __init__(self, name = "Human", job = None, home = None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50 #радість
        self.satiety = 50 #ситість
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            ...
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        ...
    def work(self):
        ...
    def shopping(self, manage):
        ...
    def chill(self):
        ...
    def clean_home(self):
        ...
    def to_repair(self):
        ...

    def days_indexes(self, day):
        ...
    def is_alive(self):
        ...
    def live(self, day):
        ...

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list (brand_list))
        self.fuel = brand_list[self.brand]["fuel"] #пальне
        self.strength = brand_list[self.brand]["strength"] #сила автівки
        self.consumption = brand_list[self.brand]["consumption"] #споживання авто

    def drive(self):
        if self.strength>0 and self.fuel>=self.consumption:
            self.fuel-=self.consumption
            self.strength -=1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0 #безлад вдома
        self.food = 0


brands_of_car = {
    "BMW":{"fuel": 100, "strength": 100, "consumption": 6 },
    "Lada":{"fuel": 50, "strength": 40, "consumption": 10 },
    "Volvo":{"fuel": 70, "strength": 150, "consumption": 8 },
    "Ferrari":{"fuel": 80, "strength": 120, "consumption": 14 },
}

job_list ={
    "Java developer": {"salary" : 50, "gladness_less": 10},
    "Python developer": {"salary" : 40, "gladness_less": 3},
    "C++ developer": {"salary" : 45, "gladness_less": 25},
    "Rust developer": {"salary" : 70, "gladness_less": 1},
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"] #зарплата
        self.gladness_less = job_list[self.job]["gladness_less"] #втрата радості
