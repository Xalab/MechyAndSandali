import time
import random


# class Arena:
#     pass
#
#
# class Shop:
#     pass
#
#
# class Travel:
#     pass


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

class Slime(Mobs):
    hp = 10
    damage = random.randint(1, 4)
    defence = 0
    xp = 5
    money = 10
    loot = ["Stick", "Gel", "Juice"]


class Forest:
    lvl = 10


class Fields:
    lvl = 1
    mobs = ["Slime"]


class Xp:
    Xp = [5, 10, 15]
    Lvl = [2, 3, 4]


class Warrior:
    name = ""
    lvl = 1
    xp = 0
    money = 0
    pwr = 1
    Dmg = random.randint(1+pwr, 4+pwr)
    Def = 1
    Hp = 10
    loot = []
    InBattle = False

    def stats(self):
        print(f"\rУровень - {self.lvl}\nДеньги - {self.money}\nЗдоровье - "
              f"{self.Hp}\nАтака - {self.pwr}\nЗащита - {self.Def}")

    def go_travel(self, location):
        if Warrior.InBattle:
            print("Вы в бою.")
        else:
            if self.lvl < location.lvl:
                print(f"Ваш уровень слишком мал, вам нужен {location.lvl} уровень.")
            elif self.lvl >= location.lvl:
                if location == Fields:
                    print("Вы вышли в поля.")
                    time.sleep(2)
                    mob = Fields.mobs[0]
                    print(f"Вы встретили {mob}")
                    if mob == "Slime":
                        fighting = Slime()
                        Warrior.InBattle = True
                        print("Перед вами прыгает маленький слаймик. Что будете делать?")
                    print("Атака/Побег")
                    do = input()
                    if do == "Атака":
                        Warrior.battle(self, mob, fighting)
                    elif do == "Побег":
                        Warrior.away(self)
                elif location == Forest:
                    print("Вы вошли в лес.")

    def away(self):
        print("Вы решили пройти мимо.")
        Warrior.InBattle = False

    def battle(self, mob, fighting_mob):
        while Player.Hp > 0 and fighting_mob.hp > 0:
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
                Warrior.Hp -= damage
                print(f"{mob} нанёс вам {damage} урона.")
            else:
                print(f"{mob} промахнулся.")
        if fighting_mob.hp <= 0:
            fighting_mob.victory()
        elif Player.Hp <= 0:
            print("Вы проиграли.")
            exit(0)


Name = input("Добро пожаловать в игру 'Мечи и Сандали!'\nВведите имя вашего героя!\n")
Player = Warrior()
Player.name = Name
print(f"Добро пожаловать, {Player.name}!")
while True:
    Do = input("--> ")
    if Do == "В лес":
        Player.go_travel(Forest)
    elif Do == "На поля":
        Player.go_travel(Fields)
    elif Do == "Статы":
        Player.stats()
