from app.main import get_human_age


def test_zero_value() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_year_before_age_one() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_animals_turning_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_year_before_age_two() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_animals_turning_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_year_before_cat_turns_three() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_year_cat_turns_three() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_animal_large_age_amount() -> None:
    assert get_human_age(100, 100) == [21, 17]
