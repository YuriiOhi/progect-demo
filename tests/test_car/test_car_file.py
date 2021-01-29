import pytest

from car.car import prettify_string, check_numeric, Car, Point, OutOfFuelException, TooMuchFuelException


@pytest.mark.parametrize('actual, expected', [
    ('toyota', 'Toyota'),
    ('toYoTa', 'Toyota'),
    ('toyoTA\n', 'Toyota'),
    ('Toyota', 'Toyota'),
    ('TOYOTA', 'Toyota')
])
def test_prettify_string(actual, expected):
    assert prettify_string(actual) == expected


def test_prettify_string_exception():
    with pytest.raises(TypeError):
        prettify_string(10000)


@pytest.mark.parametrize('actual, expected', [
    (100.0, 100.0),
    (100, 100.0),
    ('100', 100.0)
])
def test_check_numeric(actual, expected):
    assert check_numeric(actual) == expected


@pytest.mark.parametrize('value, exception_type', [
    (-100, ValueError),
    ('error', ValueError),
    (dir, TypeError)
 ])
def test_check_numeric_exception(value, exception_type):
    with pytest.raises(exception_type):
        check_numeric(value)


def test_car_constructor():
    car = Car('Toyota', 40.0, 2.0, Point())

    assert car.model == 'Toyota'
    assert car.fuel_capacity == 40.0
    assert car.fuel_consumption == 2.0
    assert car.car_location == Point()
    assert car.fuel_amount == 40.0


def test_car_to_string():
    car = Car('Toyota', 40.0, 2.0, Point())

    assert str(car) == 'The model of the car: Toyota. Fuel amount 40.0. Fuel capacity 40.0. Fuel consumption 2.0. Location: (0.0, 0.0)\n'


def test_no_fuel_exception():
    car = Car('Toyota', 40.0, 2.0, Point())
    paris = Point(20.0, 20.0)

    with pytest.raises(OutOfFuelException):
        car.drive(paris)

    with pytest.raises(TooMuchFuelException):
        car.refill(100)


def test_drive_with_cordinates():
    car = Car('Toyota', 40.0, 2.0, Point())

    with pytest.raises(OutOfFuelException):
        car.drive_with_coordinates(20.0, 200.0)


def test_refill():
    car = Car('Toyota', 40.0, 2.0, Point())
    Paris = Point(10.0, 10.0)

    assert car.fuel_amount == 40.0

    car.drive(Paris)

    assert car.fuel_amount == 11.715728752538098

    car.refill(1.0)

    assert car.fuel_amount == 12.715728752538098
