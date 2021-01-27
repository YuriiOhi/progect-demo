from typing import Any
import copy


class Complex:
    def __init__(self, re: float = 0.0, im: float = 0.0) -> None:
        self._re = float(re)
        self._im = float(im)

    @property
    def re(self) -> float:
        return self._re

    @property
    def im(self) -> float:
        return self._im

    @re.setter
    def re(self, value: float) -> None:
        self._re = float(value)

    @im.setter
    def im(self, value: float) -> None:
        self._im = float(value)

    def __str__(self) -> str:
        if self.im < 0:
            return f'({self.re}{self.im}i)'
        else:
            return f'({self.re}+{self.im}i)'

    def __eq__(self, other: Any) -> bool:
        self.__check__type(other)
        return self.re == other.re and self.im == other.im

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __check__type(self, other: Any) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError(f'other param should be of type {self.__class__.__name__}')

    def __iadd__(self, other) -> None:
        self.__check__type(other)
        self.re += other.re
        self.im += other.im

    def __isub__(self, other) -> None:
        self.__check__type(other)
        self.re -= other.re
        self.im -= other.im

    def __add__(self, other) -> Any:
        self.__check__type(other)
        tmp = copy.deepcopy(self)
        tmp.__iadd__(other)
        return tmp

    def __sub__(self, other) -> Any:
        self.__check__type(other)
        tmp = copy.deepcopy(self)
        tmp.__isub__(other)
        return tmp

    def __mul__(self, other) -> Any:
        tmp = copy.deepcopy(self)

        tmpRe = tmp.re * other.re - tmp.im * other.im
        tmpIm = tmp.re * other.im + tmp.im * other.re

        tmp.re = tmpRe
        tmp.im = tmpIm
        return tmp

if __name__ == '__main__':  # pragma: no cover
    complex = Complex(0.0, 0.0)
    complex2 = Complex(1.2, -3.2)

    complex3 = complex.__mul__(complex2)

    print(complex)
    print(complex2)
    print(complex3)
