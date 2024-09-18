import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('1', 1, 1),
    ('3851929443', 1, 9),
    ('3851929443', 2, 40),
    ('3851929443', 3, 162),
    ('3851929443', 4, 648),
    ('3851929443', 5, 2592),
    ('3851929443', 6, 7776),
    ('3851929443', 7, 25920),
    ('3851929443', 8, 103680),
    ('3851929443', 9, 311040),
    ('3851929443', 10, 933120),
]


@pytest.mark.parametrize('sequence, span, expected', testdata)
def test_run(sequence, span, expected):
    assert main.max_product(sequence, span) == expected


def test_max_product_fails_when_span_is_larger_than_sequence():
    with pytest.raises(ValueError):
        main.max_product('123', 4)


def test_max_product_fails_when_span_is_negative():
    with pytest.raises(ValueError):
        main.max_product('123', -4)


def test_max_product_fails_when_sequence_is_not_numeric():
    with pytest.raises(ValueError):
        main.max_product('1A2B3C', 2)
