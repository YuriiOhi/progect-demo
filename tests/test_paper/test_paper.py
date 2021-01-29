import pytest

from pen_paper.paper import check_numeric, Paper, OutOfSpaceException


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


def test_paper_constructor():
    paper = Paper(10)

    assert paper.max_symbols == 10
    assert paper.symbols == 0
    assert paper.content == ''


def test_show():
    paper = Paper(10)

    paper.add_content('happy holiday')
    paper.show()


def test_add_content():
    paper = Paper(10)
    message = 'hello'

    paper.add_content(message)
    symbols_available = paper.max_symbols - paper.symbols

    assert symbols_available == 5


def test_out_of_space_exception():
    paper = Paper(10)

    message = 'Launching pytest with argument'
    message2 = 'Hello'

    paper.add_content(message)

    with pytest.raises(OutOfSpaceException):
        paper.add_content(message2)
