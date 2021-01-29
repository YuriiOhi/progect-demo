import pytest

from pen_paper.paper import Paper
from pen_paper.pen import check_numeric, Pen, OutOfInkException


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


def test_pen_constructor():
    pen = Pen(10)

    assert pen.ink_amount == 10
    assert pen.ink_capacity == 10


def test_refill():
    pen = Pen(10)
    paper = Paper(10)

    pen.write(paper, '12345')

    assert pen.ink_amount == 5

    pen.refill()

    assert pen.ink_amount == 10


def test_out_of_space_exception():
    pen = Pen(10)
    paper = Paper(10)

    message = 'Launching pytest with argument'
    message2 = 'Hello'

    pen.write(paper, message)

    with pytest.raises(OutOfInkException):
        pen.write(paper, message2)
