# Создание переменной immutable_var с кортежем
immutable_var = (1, 2, 'a', 'b', True)
# Вывод кортежа на экран
print("Immutable tuple:", immutable_var)

# Попытка изменить элементы кортежа
try:
    immutable_var[0] = 100  # Попытка изменить первый элемент
except TypeError as e:
    print("Ошибка:", e)
    print("Нельзя изменить значения элементов кортежа, потому что кортежи (tuple) являются неизменяемыми структурами данных в Python.")

# Создание изменяемой структуры данных
mutable_list = [1, 2, 3, 4, 'Hello', 'String', True]
print("mutable list:", mutable_list)
# Изменение элементов в списке
mutable_list[0] = 100
mutable_list[5] = 'world'
print("mutable list:", mutable_list)
