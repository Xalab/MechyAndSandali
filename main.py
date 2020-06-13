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
        "Поножи": {"Джинсы": 7, "Шорты в горошек": 3},
        "Шляпа": {"Кепка": 1},
        "Перчатки": {"Кожаные перчатки": 4},
        "Еда": {"Булка": 5}
    }
    items_cost = {"Деревянная палка": 10,
                  "Ведро": 15,
                  "Шлёпки": 5,
                  "Ватник": 25,
                  "Джинсы": 30,
                  "Шорты в горошек": 15,
                  "Кепка": 5,
                  "Кожаные перчатки": 20,
                  "Булка": 2
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
                    print(f"Цена - {self.items_cost.get(item_from_shop)}")

    def buy(self, item):
        cost = self.items_cost.get(item)
        if Player.money >= cost:
            Player.money -= cost
            Player.inventory.append(item)
            print(f"Вы купили {item}")
        else:
            print("У вас не хватает денег.")


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
        Player.inventory += drop
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
    money = 1
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

    def get_inventory(self):
        if len(self.inventory) > 0:
            print(self.inventory)
        else:
            print("У вас ничего нет в инвентаре.")

    def get_equipment(self):
        for equip in self.equipped:
            print(equip, end=" --> ")
            print(self.equipped.get(equip))

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
            self.pwr += 1
            self.Def += 1
            print("У нас новый уровень!")
            print(f"Сейчас у вас {self.lvl} уровень!")
            print(f"До следующего уровня вам нужно набрать {Xp.Xp[self.lvl]} очков опыта!")

    def equip(self, item):
        if item in self.inventory:
            for global_item in Shop.items.values():
                if item in global_item.keys():
                    result = get_key(Shop.items, global_item)
            if not self.is_equipped.get(result):
                self.equipped.update({result: item})
                self.is_equipped.update({result: True})
                for global_item in Shop.items.values():
                    if item in global_item.keys():
                        bonus = global_item.get(item)
                self.Dmg = random.randint(1 + self.pwr, 4 + self.pwr) + bonus
                print("Предмет экипирован.")
            elif self.is_equipped.get(result):
                if self.equipped.get(result) == item:
                    print("Этот предмет уже экипирован.")
                else:
                    print("У вас экипирован другой предмет. Заменить?")
                    answer = input()
                    if answer.lower() == "да":
                        self.equipped.fromkeys({result: item})
                        self.is_equipped.fromkeys({result: True})
                        for global_item in Shop.items.values():
                            bonus = global_item.get(item)
                        self.Dmg = random.randint(1 + self.pwr, 4 + self.pwr) + bonus
                        print("Предмет экипирован.")
        else:
            print("У вас нет такого предмета.")


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
        print("\n--> В поля <--\nОтправляет вас в поля\n\n--> Статы <--\nПоказывает характеристики"
              "\n\n-->Экипировать<--\nПозволяет экипировать предмет из инвентаря\n\n-->Инвентарь<--"
              "\nОтображает ваш инвентарь\n\n-->Экипировка<--\nОтображает вашу экипировку")


Chernyahov_Shop = Shop()
Chernyahov_Shop.items_in_shop.append("Деревянная палка")
Chernyahov_Shop.items_in_shop.append("Ведро")
Chernyahov_Shop.items_cost.get("Деревянная палка")

Name = input("Добро пожаловать в игру 'Мечи и Сандали!'\nВведите имя вашего героя!\n")
Player = Warrior()
Player.name = Name
print(f"Добро пожаловать, {Player.name}!")
print("Вы находитесь в деревне Черняхов. Это ваша стартовая локация.")
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
    elif Do.lower() == "help":
        Help()
    elif Do.lower() == "инвентарь":
        Player.get_inventory()
    elif Do.lower() == "экипировка":
        Player.get_equipment()
    elif "экипировать" in Do.lower():
        print("Что вы хотите экипировать?")
        Equip = input()
        Player.equip(Equip)
    elif Do.lower() == "в магазин":
        Chernyahov_Shop.shop_goods()
        print("Вы хотите что-то купить?")
        item = input()
        Chernyahov_Shop.buy(item)


