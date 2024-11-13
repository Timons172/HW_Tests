import pytest
from functions import solve, fio, vote


def test_solve():
    phrases = [
        "нажал кабан на баклажан",
        "рвал дед лавр",
        "азот калий и лактоза",
        "а собака боса",
        "тонет енот",
        "пуст суп"
    ]
    result = solve(phrases)
    assert result == phrases


@pytest.mark.parametrize(
    'fio_list, initials',
    (
        (['Иванов', 'Иван', 'Иванович'], 'ИИИ'),
        (['Жан', 'Кот', 'Вандамович'], 'ЖКВ'),
        (['Павлов', 'Иван', 'Уралович'], 'ПИУ'),
        (['Семейный', 'Доминик', 'Торретович'], 'СДТ'),
    )
)
def test_fio(fio_list, initials):
    assert fio(fio_list) == initials


@pytest.mark.parametrize(
    'votes, winner',
    (
        ([1,1,1,2,3], 1),
        ([3,2,3,3,2], 3),
    )
)
def test_vote(votes, winner):
    assert vote(votes) == winner
