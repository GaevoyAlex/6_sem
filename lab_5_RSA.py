import rsa
import random
import string

# Функция для генерации случайных сообщений заданной длины
def generate_random_message(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

# Функция для тестирования алгоритма RSA
def test_rsa(num_tests):
    # Генерация ключей
    public_key, private_key = rsa.newkeys(1024)

    for i in range(num_tests):
        message = generate_random_message(random.randint(1, 100))
        encrypted_message = rsa.encrypt(message.encode(), public_key)
        decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()

        print(f"Тест {i+1}:")
        print(f"Оригинальное сообщение: {message}")
        print(f"Зашифрованное сообщение: {encrypted_message}")
        print(f"Расшифрованное сообщение: {decrypted_message}")

        if message != decrypted_message:
            print("Результат: Тест провален.")
            return
        else:
            print("Результат: Тест пройден успешно.")

    print(f"Все {num_tests} тестов пройдены успешно.")

# Вызов функции тестирования
if __name__ == '__main__':
    test_rsa(10)
