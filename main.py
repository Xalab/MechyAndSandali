import time
import random


def dots_pause(reverse):
    for i in range(int(reverse)):
        time.sleep(0.3)
        print("\r.")
        time.sleep(0.3)
        print("\r..")
        time.sleep(0.3)
        print("\r...")


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

    def away(self):
        print("Вы решили пройти мимо.")
        Warrior.InBattle = False

    def battle(self, mob, fighting_mob):
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


class Start:

    @staticmethod
    def first_stage():
        print("Вы много путешествовали, набирая силы и барахло.")
        time.sleep(1.2)
        print("Однако, в таверне услыхали о том, якобы на вашу родину ересь нечистая клыки точит.")
        time.sleep(1.2)
        print("Не долго думая, вы взяли весь свой шмот, и отправились в родные края.")
        dots_pause(3)
        print("На границе вы узнали, что на ваш родной край напала соседнее государство.")
        time.sleep(2)
        print("Вас политика не сильно заботила, вы промолчали.")
        time.sleep(2)
        dots_pause(3)
        print("Вы были на подъезде к вашей деревне, но вруг на дороге стало слишком тихо...")
        print("Вы думаете, как поступить дальше...")
        quest1 = input("Затаиться и осмотреться - 0. Крикнуть 'КТО ТУТ? Я ВАС ЧУЮ!' - 1 ")
        if quest1:
            print("Вы закричали на весь лес. Вам стало казаться что вам не следовало выпивать сразу весь ром по дороге.")
            print("Вы крикнули еще раз, но на ваши крики никто не отвечал, это вас насторожило.")
            print("Вы тихо сошли с дороги, от того места где кричали, и решили затаиться так, чтобы лицезреть дорогу.")
            print("Вы затаились только 10 минут назад, но тут вы начали слышать шуршание листьев вокруг вас.")
            quest2 = input("Оккуратно высунуться и увидеть того, кто тут топчеться. - 0."
                           "\nВыпрыгнуть из засады и ударить со всей силы супостата! - 1."
                           "\nЗатаиться еще сильней. Лучше быть осторожным. - 2. ")
            if not quest2:
                print("Вы подняли вашу голову, чтобы увидеть крадущегося...")
                print("Едва вы высунулись, вам прилетела стрела в голову.")
                print("На этом ваше путешествие закончилось.")
                print("--- Вы погибли ---")
                print("--- Конец игры ---")
            elif quest2 == 1:
                print("Вы выпрыгнули и со всей силы вмазали супостату.")
                print("Так как смеркало, вы не сумели разглядеть как следует вашу жертву, но поняли одно - "
                      "он был не обычный бандит.")
                print("Это был одетый в кольчугу лучник, который целился в вас еще задолго до того, как вы спрятались.")
                print("Всё же не стоило кричать - подумали вы.")

        elif not quest1:
            print("Вы решили затаиться и осмотреться.")
        time.sleep(0)
        print()

    def second_stage(self):
        pass

    def third_stage(self):
        pass


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
Start.first_stage()
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

