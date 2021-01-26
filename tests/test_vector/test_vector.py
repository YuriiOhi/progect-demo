import pytest

from vector.vector import Vector


@pytest.mark.parametrize('x, y', [
    (0.0, 0.0),
    (1.0, 3.0)
])
def test_vector_constructor(x, y):
    vector = Vector(x, y)
    assert vector.x == x
    assert vector.y == y


def test_vector_setters():
    vector = Vector()

    vector.x = 42
    vector.y = 42

    assert vector.x == 42.0
    assert vector.y == 42.0


@pytest.mark.parametrize('value, exception_type', [
    ('error', ValueError),
    (dir, TypeError)
])
def test_vector_setters_exception(value, exception_type):
    vector = Vector()

    with pytest.raises(exception_type):
        vector.x = value

    with pytest.raises(exception_type):
        vector.y = value


def test_vector_length():
    v1 = Vector(1.1, 1.1)

    assert v1.length() == 1.5556349186104048


def test_vector_to_string():
    vector = Vector()

    assert str(vector) == '(0.0, 0.0)'


def test_vector_operators():
    v1 = Vector()
    v2 = Vector()
    v3 = Vector(1.1, 2.2)

    assert v1 == v2
    assert not v1 == v3
    assert not v1 != v2
    assert v1 != v3
    assert v1 + v3
    assert v1 - v3


def test_vector_check_type_exception():
    with pytest.raises(TypeError):
        v1 = Vector(1.1, 2.2)
        v2 = 'qwerty'

        assert v1 == v2
