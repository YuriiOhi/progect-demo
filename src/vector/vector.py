from typing import Any
from math import hypot


class Vector:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, value: float) -> None:
        self._x = float(value)

    @y.setter
    def y(self, value: float) -> None:
        self._y = float(value)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: Any) -> bool:
        self.__check__type(other)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __check__type(self, other: Any) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError(f'other param should be of type {self.__class__.__name__}')

    def length(self) -> float:
        return hypot(self.x, self.y)

    def __iadd__(self, other) -> None:
        self.__check__type(other)
        self.x += other.x
        self.y += other.y

    def __isub__(self, other) -> None:
        self.__check__type(other)
        self.x -= other.x
        self.y -= other.y

    def __add__(self, other) -> Any:
        self.__check__type(other)
        tmp = self
        tmp.__iadd__(other)
        return tmp

    def __sub__(self, other) -> Any:
        self.__check__type(other)
        tmp = self
        tmp.__isub__(other)
        return tmp


if __name__ == '__main__':  # pragma: no cover
    vector = Vector(1.1, 1.1)
    vector2 = Vector(2.2, 2.2)
    vector3 = vector.__add__(vector2)

    print(vector3)
