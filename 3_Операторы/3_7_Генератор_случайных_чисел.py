import random
for i in range(10):
    print(random.randint(1, 50), end=" ")
print()
numbers = [1, 2, 3, 4, 5]
# Перемешать список
random.shuffle(numbers)
print(numbers)
# Случайный элемент из списка
print(random.choice(numbers))