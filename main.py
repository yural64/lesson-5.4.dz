# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
#
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа
# открытости/закрытости (Open/Closed Principle), одного из пяти SOLID принципов
# объектно-ориентированного программирования. Принцип гласит, что программные сущности
# (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
#
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для
# борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко можно
# было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
#
# Исходные данные:
# - Есть класс `Fighter`, представляющий бойца.
# - Есть класс `Monster`, представляющий монстра.
# - Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
#
# Шаг 1:Создайте абстрактный класс для оружия
# - Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.
#
# Шаг 2: Реализуйте конкретные типы оружия
# - Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`.
# Каждый из этих классов реализует метод `attack()` своим уникальным способом.
#
# Шаг 3: Модифицируйте класс `Fighter`
# - Добавьте в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
# - Добавьте метод `change_weapon()`, который позволяет изменить оружие бойца.
#
# Шаг 4: Реализация боя
# - Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя
# из выбранного оружия.
#
# Требования к заданию:
#
# - Код должен быть написан на Python.
# - Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия
# можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# - Программа должна выводить результат боя в консоль.
#
# Пример результата:
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр побежден!
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр побежден!

from abc import ABC, abstractmethod

class Weapon(ABC):

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")

class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука")

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())


class Monster():
    pass

# Объекты меч и лук
sword = Sword()
bow = Bow()

# Боец с мечом
fighter = Fighter(sword())

# Боец бьет мечом
fighter.fight()

# Боец меняет оружие
fighter.changeWeapon(bow)

# Боец стреляет из лука
fighter.fight()
