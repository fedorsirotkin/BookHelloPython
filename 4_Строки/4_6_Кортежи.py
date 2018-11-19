# Кортеж - Школьный рюкзак
books = ("Математика", "Литература", "Рисование")

print("Вывод кортежа функцией print():")
print(books)

print("Поэлементный перебор кортежа:")
for book in books:
    print(book)

print("Сейчас у тебя ", len(books), " учебника")

book = input("Поиск учебника: ")
if book in books:
    print("Учебник в рюкзаке")
else:
    print("Учебника ", book, " в рюкзаке нет")

# Слияние кортежей
new_books = ("Музыка", "Русский язык")
all_books = books + new_books
print("Результат слияния:")
print(all_books)