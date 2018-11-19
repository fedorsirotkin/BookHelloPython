# Открытие файла
txt = open("Программирование.txt", "a", encoding="utf-8")
# Запись в файл
txt.write("\nДобавим еще одну строчку")
# Закрытие файла
txt.close()

# Открытие файла
txt = open("Программирование.txt", "r", encoding="utf-8")
# Чтение файла
content = txt.read()
# Содержимое файла
print(content)
# Закрытие файла
txt.close()