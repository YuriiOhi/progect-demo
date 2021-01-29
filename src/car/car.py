from point.point import Point


def prettify_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f'value should be of type str: {value}')

    value = value.strip().lower()
    value = value.capitalize()
    return value


def check_numeric(value: float):
    value = float(value)
    if value < 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class OutOfFuelException(Exception):
    pass


class TooMuchFuelException(Exception):
    pass


class Car:
    def __init__(self, model: str, capacity: float, consumption: float, location: Point) -> None:
        self._car_model = prettify_string(model)
        self._fuel_capacity = check_numeric(capacity)
        self._fuel_consumption = check_numeric(consumption)
        self._car_location = location
        self._fuel_amount = check_numeric(capacity)

    @property
    def model(self) -> str:
        return self._car_model

    @property
    def fuel_amount(self) -> float:
        return self._fuel_amount

    @property
    def fuel_capacity(self) -> float:
        return self._fuel_capacity

    @property
    def fuel_consumption(self) -> float:
        return self._fuel_consumption

    @property
    def car_location(self) -> Point:
        return self._car_location

    def check_fuel(self) -> None:
        if self.fuel_amount <= 0:
            raise OutOfFuelException()

    def __str__(self) -> str:
        return f'The model of the car: {self.model}. Fuel amount {self.fuel_amount}. Fuel capacity {self.fuel_capacity}. Fuel consumption {self.fuel_consumption}. Location: {self.car_location}\n'

    def drive(self, destination: Point) -> None:
        distance = self._car_location.distance(destination)
        fuel_needed = self._fuel_consumption * distance

        self.check_fuel()

        self._car_location = destination
        self._fuel_amount -= fuel_needed

        self.check_fuel()

        print('Car has arrived to the destination: ', destination)

    def drive_with_coordinates(self, x: float, y: float) -> None:
        destination = Point(x, y)

        self.drive(destination)

    def refill(self, fuel: float) -> None:
        max_refill_volume = self.fuel_capacity - self.fuel_amount

        if fuel > max_refill_volume:
            raise TooMuchFuelException()

        self._fuel_amount += fuel
        print('Car was successfully refilled!')


if __name__ == '__main__':  # pragma: no cover
    car1 = Car('BMW', 40.0, 2.0, Point())
    Paris = Point(10.0, 10.0)
    print(car1)
    print('-------------------')

    car1.drive(Paris)
    print(car1)
    print('-------------------')

    car1.refill(10.0)

    print(car1)
    print('-------------------')
    car1.refill(5.0)

    car1.drive_with_coordinates(2.0, 10.0)

    print(car1)
    print('-------------------')
