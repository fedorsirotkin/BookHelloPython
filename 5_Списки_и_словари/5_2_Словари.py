# Создание словаря
dict = {
    "apple" : "яблоко",
    "bold" : "жирный",
    "bus" : "автобус",
    "cat" : "кошка",
    "car" : "машина"
}

# Печать словария
print(dict)
for item in dict:
    print(item, " => ", dict[item])

# Дополнение словаря
dict["test"] = "Тест"
print(dict)

# Сокращение словаря
del dict["bus"]
print(dict)