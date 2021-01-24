def prettify_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f'value should be of type str: {value}')

    value = value.strip().lower()
    value = value.capitalize()
    return value


def check_numeric(value: int) -> object:
    value = int(value)
    if value <= 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class UnitIsDeadException(Exception):
    pass

class Unit:
    def __init__(self, name: str, hp: int, dmg: int) -> None:
        self._name = prettify_string(name)
        self._hp = check_numeric(hp)
        self._maxHP = check_numeric(hp)
        self._dmg = check_numeric(dmg)


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
    def dmg(self) -> int:
        return self._dmg

    @hp.setter
    def hp(self, value) -> None:
        self._hp = check_numeric(value)

    @hp.setter
    def dmg(self, value) -> None:
        self._dmg = check_numeric(value)

    def add_hit_points(self, value) -> None:
        self.__ensure_is_alive(self)
        self._hp += check_numeric(value)
        if self._hp > self._maxHP:
            self._hp = self._maxHP

    def take_damage(self, value) -> None:
        self.__ensure_is_alive(self)
        self._hp -= check_numeric(value)

    def attack(self, value) -> None:
        enemy = Unit(value)
        enemy.take_damage(self._dmg)
        enemy.counter_attack(self)

    def counter_attack(self, value ) -> None:
        enemy = Unit(value)
        enemy.take_damage(self._dmg / 10)

    def __str__(self) -> str:
        return f'{self.name}: ({self.hp}/{self.maxHP}), damage = {self.dmg}.'

    def __ensure_is_alive(self):
        if self.hp == 0:
            raise UnitIsDeadException()


if __name__ == '__main__':  # pragma: no cover
    unit = Unit('SoLdIeR', 100, 10)


    print(unit)


