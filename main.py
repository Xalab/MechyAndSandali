import time
import random
from story import *


class Mobs:
    hp = 0
    damage = 0
    defence = 0
    xp = 0
    money = 0
    loot = []

    def victory(self):
        print("Вы победили!")
        time.sleep(0.5)
        Player.money += self.money
        Player.xp += self.xp
        drop = self.loot[random.randint(0, len(self.loot))]
        Player.loot += drop
        print(f"Вы получили {self.xp} xp, {self.money} монет.\nА так же вам выпало: {drop}.")
        Player.lvl_up()


class Slime(Mobs):
    hp = 10
    damage = random.randint(1, 4)
    defence = 0
    xp = 5
    money = 10
    loot = ["Stick", "Gel", "Juice"]

    @staticmethod
    def meeting():
        Warrior.InBattle = True
        print("Перед вами прыгает маленький слаймик. Что будете делать?")


class Fields:
    lvl = 1
    mobs = ["Slime"]

    @staticmethod
    def enter_location():
        print("Вы вышли в поля.")
        time.sleep(2)
        mob = Fields.mobs[random.randint(0, len(Fields.mobs) - 1)]
        print(f"Вы встретили {mob}")
        time.sleep(1)
        if mob == "Slime":
            fighting = Slime()
            Slime.meeting()
        print("Атака/Побег")
        do = input()
        if do == "Атака":
            Warrior.battle(mob, fighting)
        elif do == "Побег":
            Warrior.away()


class Xp:
    Xp = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]


class Warrior:
    name = ""
    lvl = 1
    xp = 0
    money = 0
    pwr = 1
    Dmg = random.randint(1+pwr, 4+pwr)
    Def = 1
    hp = 10
    max_hp = 10
    loot = []
    InBattle = False

    def stats(self, param):
        if param.lower() == "уровень":
            print(f"Сейчас у вас {self.lvl} уровень и {self.xp} очков опыта.")
        elif param.lower() == "характеристики":
            print(f"Сила - {self.pwr}.\nЗащита - {self.Def}.\nЗдоровье - {self.hp} из {self.max_hp}.")
        elif param.lower() == "баланс":
            print(f"Сейчас у вас {self.money} монет.")

    def go_travel(self, location):
        if Warrior.InBattle:
            print("Вы в бою.")
        else:
            if self.lvl < location.lvl:
                print(f"Ваш уровень слишком мал, вам нужен {location.lvl} уровень.")
            elif self.lvl >= location.lvl:
                if location == Fields:
                    Fields.enter_location()

    @staticmethod
    def away():
        print("Вы решили пройти мимо.")
        Warrior.InBattle = False

    @staticmethod
    def battle(mob, fighting_mob):
        while Player.hp > 0 and fighting_mob.hp > 0:
            if fighting_mob.hp <= 0:
                print(f"{mob} был повержен")
            time.sleep(0.5)
            print(f"Вы замахнулись на {mob}.")
            time.sleep(0.5)
            if random.randint(0, 1):
                fighting_mob.hp -= Warrior.Dmg
            elif not random.randint(0, 1):
                print("Вы промахнулись.")
            time.sleep(0.5)
            if fighting_mob.hp <= 0:
                break
            print(f"У {mob} осталось {fighting_mob.hp} hp.")
            time.sleep(0.5)
            print(f"{mob} замахнулся на вас.")
            time.sleep(0.5)
            if random.randint(0, 1):
                damage = fighting_mob.damage
                Warrior.hp -= damage
                print(f"{mob} нанёс вам {damage} урона.")
            else:
                print(f"{mob} промахнулся.")
        if fighting_mob.hp <= 0:
            fighting_mob.victory()
        elif Player.hp <= 0:
            print("Вы проиграли.")
            exit(0)

    def lvl_up(self):
        xp_for_next_lvl = Xp.Xp[self.lvl]
        if self.xp >= xp_for_next_lvl:
            self.xp -= xp_for_next_lvl
            self.lvl += 1
            print("У нас новый уровень!")
            print(f"Сейчас у вас {self.lvl} уровень!")
            print(f"До следующего уровня вам нужно набрать {Xp.Xp[self.lvl]} очков опыта!")


class Difficult:

    def easy(self):
        pass

    def normal(self):
        pass

    def hard(self):
        pass


class Help:

    def __init__(self):
        print("Что вы хотите узнать?")
        print("\n--- Команды ---")
        request = input()
        if request.lower() == "команды":
            self.commands()

    def commands(self):
        print("\n--> В поля <--\nОтправляет вас в поля\n\n--> Статы <--\nПоказывает характеристики")


Name = input("Добро пожаловать в игру 'Мечи и Сандали!'\nВведите имя вашего героя!\n")
Player = Warrior()
Player.name = Name
print(f"Добро пожаловать, {Player.name}!")
while True:
    Do = input("--> ")
    if Do.lower() == "в поля":
        Player.go_travel(Fields)
    elif Do.lower() == "статы":
        print("Укажите какие статы вы хотите увидеть")
        print("--- Уровень ---\n--- Характеристики ---\n--- Баланс ---")
        stat = input()
        if stat.lower() == "уровень":
            Player.stats("уровень")
        elif stat.lower() == "характеристики":
            Player.stats("характеристики")
        elif stat.lower() == "баланс":
            Player.stats("баланс")
    elif Do.lower() == "help":
        Help()

