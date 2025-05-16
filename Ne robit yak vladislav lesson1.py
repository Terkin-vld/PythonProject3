import random

class City:
    def __init__(self, name):
        self.name = name
        self.citizens = []

    def add_citizen(self, person):
        self.citizens.append(person)
        print(f"🏙️ {person.name} оселився в місті {self.name}")

class Pet:
    def __init__(self, name):
        self.name = name
        self.gladness = 50

    def play(self):
        print(f"🐶 {self.name} хоче погратись!")
        self.gladness += 5

    def eat(self):
        print(f"🍖 {self.name} їсть")
        self.gladness += 3

    def mood(self):
        print(f"Настрій {self.name}: {self.gladness}")

class Student:
    def __init__(self, name, pet, city):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True
        self.pet = pet
        self.city = city
        self.city.add_citizen(self)

    def to_study(self):
        print("📚 Час вчитись")
        self.progress += 0.12
        self.gladness -= 5

    def to_work(self):
        print("💸 Підробіток")
        self.money += 20
        self.gladness -= 3
        self.progress -= 0.02

    def to_chill(self):
        if self.money >= 10:
            print("🎉 Час відпочити (мінус 10 грн)")
            self.gladness += 8
            self.progress -= 0.05
            self.money -= 10
        else:
            print("😞 Немає грошей на розваги")

    def to_eat(self):
        if self.money >= 15:
            print("🍔 Поїв")
            self.gladness += 5
            self.money -= 15
        else:
            print("😞 Немає грошей на їжу")

    def to_play_with_pet(self):
        print(f"{self.name} грається з {self.pet.name}")
        self.gladness += 7
        self.pet.play()

    def end_of_day(self):
        print(f"Статус {self.name}: Настрій {self.gladness}, Успішність {round(self.progress, 2)}, Гроші {self.money}")
        self.pet.mood()
        print("="*40)

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
            self.to_play_with_pet()
        elif dice == 3:
            self.to_chill()
        elif dice == 4:
            self.to_work()
        elif dice == 5:
            self.to_eat()

        self.end_of_day()
        self.is_alive()


# Симуляція на 365 днів
city = City("Львів")

student1 = Student("Марко", Pet("Барсик"), city)
student2 = Student("Аліна", Pet("Рекс"), city)

for day in range(1, 366):
    if not student1.alive and not student2.alive:
        break
    print(f"=== День {day} ===")
    if student1.alive:
        student1.live(f"День {day}")
    if student2.alive:
        student2.live(f"День {day}")

print(f"\nУ місті {city.name} мешкає {len(city.citizens)} осіб.")