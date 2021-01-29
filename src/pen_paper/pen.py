from pen_paper.paper import Paper


def check_numeric(value: int):
    value = int(value)
    if value < 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class OutOfInkException(Exception):
    pass


class Pen:
    def __init__(self, ink_capacity: int):
        self._ink_capacity = check_numeric(ink_capacity)
        self._ink_amount = check_numeric(ink_capacity)

    @property
    def ink_amount(self) -> int:
        return self._ink_amount

    @property
    def ink_capacity(self) -> int:
        return self._ink_capacity

    def refill(self):
        self._ink_amount = self._ink_capacity

    def write(self, paper: Paper, message: str):
        substring = message

        if self.ink_amount <= 0:
            raise OutOfInkException()

        if len(message) > self.ink_amount:
            substring = message[0:self.ink_amount]

        self._ink_amount -= len(substring)
        paper.add_content(substring)


if __name__ == '__main__':  # pragma: no cover

    pen = Pen(20)
    paper = Paper(10)

    pen.write(paper, 'The built-in exceptir a tuple !')
    paper.show()
