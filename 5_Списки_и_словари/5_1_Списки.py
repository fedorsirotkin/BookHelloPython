# Объявление списка
books = ["Математика", "Литература", "Рисование"]

# Печать списка
print("Проверим, что у нас в рюкзаке:")
for book in books:
    print(book)

# Длина списка
print("Сейчас в рюкзаке ", len(books), " учебника")

# Поиск в списке
book = input("Поиск учебника: ")
if book in books:
    print("Учебник в рюкзаке")
else:
    print("Учебника ", book, " в рюкзаке нет")

# Соединение списка
new_books = ["Английский", "История"]
books += new_books
print(books)

# Изменение списка
books[0] = "Биология"
print(books)

# Удаление элемента списка
del books[2]
print(books)