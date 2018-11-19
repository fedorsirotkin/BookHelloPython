# Возвращаемые значения
def sum_two_num(a, b):
    return a + b


def yn(message):
    resp = None
    while resp not in ("да", "нет"):
        resp = input(message).lower()
    return resp


# Документирующие строки
def warning(message):
    """
    Выводит сообщение, заданное параметром message,
    обрамленное символами * для привлечения внимания
    :param message: сообщение
    """
    print("*" * 10, message, "*" * 10)

print(sum_two_num(2, 2))

answer = yn("Выключить будильник? [да/нет]: ")
print("Твой выбор: ", answer)

warning("Тестовое сообщениеда")
