def check_numeric(value: int):
    value = int(value)
    if value < 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class OutOfSpaceException(Exception):
    pass


class Paper:
    def __init__(self, max_symbols: int):
        self._max_symbols = check_numeric(max_symbols)
        self._symbols = 0
        self._content = ''

    @property
    def max_symbols(self) -> int:
        return self._max_symbols

    @property
    def symbols(self) -> int:
        return self._symbols

    @property
    def content(self) -> str:
        return self._content

    def show(self) -> None:
        print(self.content)

    def add_content(self, message: str):
        symbols_available = self.max_symbols - self.symbols
        sub_string = message

        if symbols_available <= 0:
            raise OutOfSpaceException()

        if len(message) > symbols_available:
            sub_string = message[0:symbols_available]

        self._symbols += len(sub_string)
        self._content += sub_string
