vowels = "аоиеёыуэюя"
text = input("Введите строку: ")
new_text = ""
for letter in text:
    if letter.lower() not in vowels:
        new_text += letter
        print("Создана новая строка: ", new_text)

print()
print("Окончательный результат: ", new_text)