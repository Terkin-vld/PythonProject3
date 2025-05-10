import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("📚 Час вчитись")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("😴 Час поспати")
        self.gladness += 4

    def to_chill(self):
        if self.money >= 10:
            print("🎉 Час відпочити (мінус 10 грн)")
            self.gladness += 8
            self.progress -= 0.05
            self.money -= 10
        else:
            print("😞 Хотів відпочити, але немає грошей")

    def to_work(self):
        print("💸 Підробіток (+20 грн)")
        self.money += 20
        self.gladness -= 3
        self.progress -= 0.02

    def to_eat(self):
        if self.money >= 15:
            print("🍔 Поїв (-15 грн, +5 настрою)")
            self.gladness += 5
            self.money -= 15
        else:
            print("😞 Немає грошей поїсти")

    def is_alive(self):
        if self.progress < -0.5:
            print("❌ Відраховано…")
            self.alive = False
        elif self.gladness <= 0:
            print("❌ Депресія…")
            self.alive = False
        elif self.progress > 5:
            print("🎓 Закінчив екстерном!")
            self.alive = False
        elif self.money < -50:
            print("❌ Борги, довелось кинути навчання…")
            self.alive = False

    def end_of_day(self):
        print(f"Статус {self.name}:")
        print(f"Настрій: {self.gladness}")
        print(f"Успішність: {round(self.progress, 2)}")
        print(f"Гроші: {self.money}")
        print("="*40)

    def live(self, day):
        print(f"{day:=^40}")
        dice = random.randint(1, 5)

        if self.gladness < 20:
            if self.money >= 10:
                self.to_chill()
            else:
                self.to_work()
        elif self.progress < 1:
            self.to_study()
        elif self.money < 20:
            self.to_work()
        elif dice == 1:
            self.to_study()
        elif dice == 2:
            self.to_sleep()
        elif dice == 3:
            self.to_chill()
        elif dice == 4:
            self.to_work()
        elif dice == 5:
            self.to_eat()

        self.end_of_day()
        self.is_alive()


# Запуск симуляції студента на рік
nick = Student("Nick")

for day in range(1, 366):
    if not nick.alive:
        break
    nick.live(f"Day {day}")