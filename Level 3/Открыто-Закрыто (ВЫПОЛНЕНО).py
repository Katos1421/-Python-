# Программа Открыто/Закрыто
# Демонстрирует работу условия else

print('Добро пожаловать снова. Попробуйте ввести пароль на этот раз!')

password=input('Введите пароль: ')
if password == "secret":
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

input('\nНажмите Enter, чтобы выйти')