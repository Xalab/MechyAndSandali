import time
import random
from story import *


def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key


class Shop:
    items_in_shop = []
    items = {
        "Меч": {"Деревянная палка": 2},
        "Шлем": {"Ведро": 1},
        "Ботинки": {"Шлёпки": 1},
        "Нагрудник": {"Ватник": 3},
        "Поножи": {"Джинсы": 2, "Шорты в горошек": 9},
        "Шляпа": {"Кепка": 1},
        "Перчатки": {"Кожаные перчатки": 1, "Не стриранные носки": 228},
        "Еда": {"Булка": 5}
    }

    def iterate_items(self):
        for item in self.items_in_shop:
            print(item, end=" ")

    def shop_goods(self):
        print("---- Товары ----")
        for item_from_shop in self.items_in_shop:
            for global_item in self.items.values():
                if item_from_shop in global_item.keys():
                    result = get_key(self.items, global_item)
                    print()
                    print(">--", result, "--<")
                    print(item_from_shop, end=" --> ")
                    if result == "Меч":
                        print("Урон: ", end="")
                    elif result == "Шлем" or "Ботинки" or "Перчатки" or "Нагрудник" or "Поножи" or "Шляпа":
                        print("Защита: ", end="")
                    elif result == "Еда":
                        print("Здоровье: ", end="")
                    print(global_item.get(item_from_shop))


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
        Player.location = "Fields"
        print("Вы вышли в поля.")
        time.sleep(2)
        mob = Fields.mobs[random.randint(0, len(Fields.mobs) - 1)]
        print(f"Вы встретили {mob}")
        time.sleep(1)
        if mob == "Slime":
            fighting = Slime()
            Slime.meeting()
        print("Атака/Побег")
        while True:
            do = input()
            if do == "Атака":
                Warrior.battle(mob, fighting)
            elif do == "Побег":
                Warrior.away()
            else:
                print("Не, оно так не работает.")
                continue
            break


class BaseLocation:
    name = "Черняхов"
    places = ["Магазин", "Таверна"]


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
    is_equipped = {"Шлем": False,
                   "Нагрудник": False,
                   "Перчатки": False,
                   "Поножи": False,
                   "Ботинки": False,
                   "Меч": False}
    equipped = {"Шлем": "Пусто",
                "Нагрудник": "Пусто",
                "Перчатки": "Пусто",
                "Поножи": "Пусто",
                "Ботинки": "Пусто",
                "Меч": "Пусто"}
    inventory = []
    InBattle = False
    location = "Черняхов"

    def stats(self, param):
        if param.lower() == "уровень":
            print(f"Сейчас у вас {self.lvl} уровень и {self.xp} очков опыта.")
        elif param.lower() == "характеристики":
            print(f"Сила - {self.pwr}.\nЗащита - {self.Def}.\nЗдоровье - {self.hp} из {self.max_hp}.")
        elif param.lower() == "баланс":
            print(f"Сейчас у вас {self.money} монет.")
        elif param.lower() == "инвентарь":
            for equip in self.equipped:
                print(equip, end=" - ")
                print(self.equipped.get(equip))

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
            self.hp = self.max_hp
            print("У нас новый уровень!")
            print(f"Сейчас у вас {self.lvl} уровень!")
            print(f"До следующего уровня вам нужно набрать {Xp.Xp[self.lvl]} очков опыта!")

    def equip(self, item):
        for global_item in Shop.items.values():
            if item in global_item.keys():
                result = get_key(Shop.items, global_item)
        if not self.is_equipped.get(result):
            self.equipped.fromkeys({result: item})
            self.is_equipped.fromkeys({result: True})
            print("Предмет экипирован.")
        if self.is_equipped.get(result):
            print("У вас экипирован другой предмет. Заменить?")
            answer = input()
            if answer.lower() == "да":
                self.equipped.fromkeys({result: item})
                self.is_equipped.fromkeys({result: True})
                print("Предмет экипирован.")


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
print("Вы находитесь в деревне Черняхов. Это ваша стартовая локация.")
Player.equip("Деревянная палка")
print("Чтобы узнать больше команд - напишите help")
while True:
    Do = input("--> ")
    if Do.lower() == "в поля":
        Player.go_travel(Fields)
    elif Do.lower() == "статы":
        print("Укажите какие статы вы хотите увидеть")
        print("--- Уровень ---\n--- Характеристики ---\n--- Баланс ---")
        stat = input()
        if stat.lower() == "уровень":
            Player.stats(stat.lower())
        elif stat.lower() == "характеристики":
            Player.stats(stat.lower())
        elif stat.lower() == "баланс":
            Player.stats(stat.lower())
        elif stat.lower() == "инвентарь":
            Player.stats(stat.lower())
    elif Do.lower() == "help":
        Help()

