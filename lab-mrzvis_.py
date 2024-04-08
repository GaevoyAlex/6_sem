# Вот простой пример балансированного конвейера для умножения целых чисел с визуализацией

def multiply(a, b):
    # Преобразуем входные целые числа в двоичные строки
    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:]

    # Определяем максимальную длину двоичных строк
    max_len = max(len(a_bin), len(b_bin))

    # Дополняем двоичные строки нулями, чтобы они были одинаковой длины
    a_bin = a_bin.zfill(max_len)
    b_bin = b_bin.zfill(max_len)

    # Инициализируем промежуточные результаты
    partial_results = [0] * max_len

    # Выполняем умножение с использованием балансированного конвейера
    for i in range(max_len):
        # Вычисляем частичное произведение для каждой позиции бита
        partial_product = int(a_bin[i]) * int(b_bin[i])
        partial_results[i] = partial_product

        # Визуализация данных на этапе конвейера
        print(f"Step {i + 1}:")
        print(f"  Data: a[{i}] = {a_bin[i]}, b[{i}] = {b_bin[i]}")
        print(f"  Partial Result: {partial_results[i]}")
        print()

    # Суммируем промежуточные результаты, чтобы получить окончательное произведение
    final_result = sum(partial_results)

    # Преобразуем окончательный результат обратно в целое число
    return final_result

# Пример использования:
a = 5
b = 3
result = multiply(a, b)
print(f"{a} * {b} = {result}")
