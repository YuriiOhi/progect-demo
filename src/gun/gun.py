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


class NotReadyException(Exception):
    pass


class OutOfRoundsException(Exception):
    pass


class Gun:
    def __init__(self, model: str, capacity: int) -> None:
        self._model = prettify_string(model)
        self._capacity = check_numeric(capacity)
        self._total_shots = 0
        self._amount = 0
        self._is_Ready = False

    @property
    def model(self) -> str:
        return self._model

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def total_shots(self) -> int:
        return self._total_shots

    def ready(self) -> bool:
        if self._is_Ready:
            return True
        else:
            return False

    def prepare(self) -> None:
        self._is_Ready = True

    def reload(self) -> None:
        self._amount = self._capacity

    def shoot(self) -> None:
        if not self._is_Ready:
            raise NotReadyException()
        if self.amount == 0:
            raise OutOfRoundsException()

        print('BANG!\n')
        self._total_shots += 1
        self._amount -= 1

    def __str__(self) -> str:
        return f'The model is: {self._model}. The amount is: {self._amount}. Total shots made: {self._total_shots}\n'


if __name__ == '__main__':  # pragma: no cover
    tt = Gun('TT', 10)
    pm = Gun('PM', 8)
    pushkin = Gun('OldGun', 1)
    pushkin.prepare()
    pushkin.ready()
    pushkin.reload()
    pushkin.shoot()

    print(pushkin)
