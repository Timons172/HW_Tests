# Функция по проверке фраз в передаваемом списке на то, являются они палиндромами или нет
def solve(phrases: list) -> list:
    result = []
    for phrase in phrases:
        phrase_strip = phrase.replace(' ', '')
        if phrase_strip == phrase_strip[::-1]:
           result.append(phrase)
    return result


# Функция, которая возвращает инициалы полного имени человека
def fio(initials: list[str]) -> str:
    return ''.join([initials[0][0], initials[1][0], initials[2][0]])


# Функция, которая возвращает число, встречающееся максимально часто
def vote(votes: list[int]) -> int:
    count_max = 0
    vote = 0
    for i in votes:
        count = votes.count(i)
        if count > count_max:
            count_max = count
            vote = i
    return vote
