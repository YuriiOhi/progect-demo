import pytest

from complex.complex import Complex


@pytest.mark.parametrize('re, im', [
    (0.0, 0.0),
    (1.0, 3.0)
])
def test_complex_constructor(re, im):
    complex = Complex(re, im)
    assert complex.re == re
    assert complex.im == im


def test_complex_setters():
    complex = Complex()

    complex.re = 42
    complex.im = 42

    assert complex.re == 42.0
    assert complex.im == 42.0


@pytest.mark.parametrize('value, exception_type', [
    ('error', ValueError),
    (dir, TypeError)
])
def test_complex_setters_exception(value, exception_type):
    complex = Complex()

    with pytest.raises(exception_type):
        complex.re = value

    with pytest.raises(exception_type):
        complex.im = value


def test_complex_to_string():
    complex = Complex()

    assert str(complex) == '(0.0+0.0i)'


def test_neg_complex_to_string():
    complex = Complex(1.1, -1.1)

    assert str(complex) == '(1.1-1.1i)'


def test_complex_operators():
    c1 = Complex()
    c2 = Complex()
    c3 = Complex(1.1, 2.2)
    c4 = Complex(2.1, 2.2)

    assert c1 == c2
    assert not c1 == c3
    assert not c1 != c2
    assert c1 != c3
    assert c1 + c3
    assert c1 - c3
    assert c3 * c4


def test_complex_check_type_exception():
    with pytest.raises(TypeError):
        c1 = Complex(1.1, 2.2)
        c2 = 'qwerty'

        assert c1 == c2
