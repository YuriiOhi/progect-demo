def prettify_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f'value should be of type str: {value}')

    value = value.strip().lower()
    value = value.capitalize()
    return value


def check_numeric(value: int):
    value = int(value)
    if value <= 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class UnitIsDeadException(Exception):
    pass


class Unit:
    def __init__(self, name: str, hp: int) -> None:
        self._name = prettify_string(name)
        self._hp = check_numeric(hp)
        self._maxHP = check_numeric(hp)

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def maxHP(self) -> int:
        return self._maxHP

    @hp.setter
    def hp(self, value) -> None:
        self._hp = check_numeric(value)

    def __str__(self) -> str:
        return f'{self.name}: ({self.hp}/{self.maxHP})'

    def __ensure_is_alive(self):
        if self.hp == 0:
            raise UnitIsDeadException()


if __name__ == '__main__':  # pragma: no cover
    unit = Unit('SoLdIeR', 100)
    print(unit)


