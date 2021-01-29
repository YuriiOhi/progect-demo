import pytest

from gun.gun import prettify_string, check_numeric, Gun, OutOfRoundsException, NotReadyException


@pytest.mark.parametrize('actual, expected', [
    ('BERETTA', 'Beretta'),
    ('beretta\n', 'Beretta'),
    ('\tBeRETtA', 'Beretta'),
    ('BereTta', 'Beretta'),
    ('Beretta', 'Beretta')
])
def test_prettify_string(actual, expected):
    assert prettify_string(actual) == expected


def test_prettify_string_exception():
    with pytest.raises(TypeError):
        prettify_string(10000)


@pytest.mark.parametrize('actual, expected', [
    (100, 100),
    (100.0, 100),
    ('100', 100)
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


def test_gun_constructor():
    beretta = Gun('Beretta', 10)

    assert beretta.model == 'Beretta'
    assert beretta.capacity == 10
    assert beretta.total_shots == 0
    assert beretta.amount == 0
    assert not beretta._is_Ready


def test_gun_to_string():
    beretta = Gun('Beretta', 10)

    assert str(beretta) == 'The model is: Beretta. The amount is: 0. Total shots made: 0\n'
    # couldn't test the string with multiple \n eg. 'The model is: Beretta\n The amount is: 0\n Total shots made: 0\n''


def test_gun_ready():
    beretta = Gun('Beretta', 10)

    assert not beretta.ready()
    beretta.prepare()

    assert beretta.ready()


def test_gun_reload():
    beretta = Gun('Beretta', 10)

    assert beretta.amount == 0

    beretta.reload()

    assert beretta.amount == 10


def test_gun_shoot():
    beretta = Gun('Beretta', 10)

    assert beretta.amount == 0
    assert beretta.total_shots == 0

    beretta.prepare()
    beretta.reload()
    beretta.shoot()

    assert beretta.amount == 9
    assert beretta.total_shots == 1


def test_gun_shoot_exception():
    beretta = Gun('Beretta', 10)

    with pytest.raises(NotReadyException):
        beretta.shoot()

    beretta.prepare()

    with pytest.raises(OutOfRoundsException):
        beretta.shoot()
