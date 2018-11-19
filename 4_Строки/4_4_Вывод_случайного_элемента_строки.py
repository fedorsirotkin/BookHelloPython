import random

word = input("Введите текст: ")

min = -len(word)
max = len(word)

position = random.randrange(min, max)
print("word[", position, "]", word[position])