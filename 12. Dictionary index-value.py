# 12. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

from random import randint

n = randint(5, 10)
print(n)

def natural_N(n):
    return {i: 3 * i + 1 for i in range(1, n)}
print(natural_N(n))

