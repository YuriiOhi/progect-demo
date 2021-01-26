from typing import Any


def prettify_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f'value should be of type str: {value}')

    value = value.strip().lower()
    value = value.capitalize()
    return value


def check_numeric(value: int):
    value = int(value)
    if value < 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class UnitIsDeadException(Exception):
    pass


class Unit:
    def __init__(self, name: str, hp: int, damage: int) -> None:
        self._name = prettify_string(name)
        self._hp = check_numeric(hp)
        self._maxHP = check_numeric(hp)
        self._damage = check_numeric(damage)

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def maxHP(self) -> int:
        return self._maxHP

    @property
    def damage(self) -> int:
        return self._damage

    @hp.setter
    def hp(self, value) -> None:
        self._hp = check_numeric(value)

    def __str__(self) -> str:
        return f'{self.name}: ({self.hp}/{self.maxHP}), dmg: {self.damage}'

    def __ensure_is_alive(self):
        if self.hp == 0:
            raise UnitIsDeadException()

    def take_damage(self, damage: int) -> None:
        self.__ensure_is_alive()

        if self.hp - damage < 0:
            self._hp = 0
            return

        self.hp -= damage

    def attack(self, enemy: Any) -> None:
        self.__ensure_is_alive()
        enemy.take_damage(self.damage)
        enemy.counter_attack(self)

    def counter_attack(self, enemy: Any) -> None:
        self.__ensure_is_alive()
        enemy.take_damage(int(self.damage / 2))


if __name__ == '__main__':  # pragma: no cover
    soldier = Unit('Soldier', 100, 20)
    warrior = Unit('Warrior', 100, 20)

    print(soldier)
    print(warrior)

    soldier.attack(warrior)

    print(soldier)
    print(warrior)
