def calculator():
    try:
        expression = input("Введите выражение для вычисления: ")
        result = eval(expression)
        print(f"Результат: {result}")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
    except Exception as e:
        print(f"Ошибка: {e}")
