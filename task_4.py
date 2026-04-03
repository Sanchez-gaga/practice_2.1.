import datetime
import os

LOG_FILE = "calculator.log"

def show_last_operations():
    """Выводит последние 5 операций из лог-файла."""
    if not os.path.exists(LOG_FILE):
        print("Лог-файл пуст или отсутствует.")
        return
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("Лог-файл пуст.")
            return
        # берём последние 5 строк
        last_lines = lines[-5:]
        print("\n--- Последние 5 операций ---")
        for line in last_lines:
            print(line.strip())
        print("-----------------------------\n")
    except Exception as e:
        print(f"Ошибка чтения лог-файла: {e}")

def log_operation(expression, result):
    """Записывает операцию в лог-файл."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {expression} = {result}\n")

def clear_log():
    """Очищает лог-файл."""
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            pass  # просто открываем в режиме записи — файл очищается
        print("Лог-файл очищен.")
    except Exception as e:
        print(f"Ошибка очистки лог-файла: {e}")

def calculate():
    """Основная логика калькулятора."""
    print("Добро пожаловать в калькулятор с логированием!")
    print("\nВведите 'clear' для очистки лога, 'exit' для выхода.")
    show_last_operations()

    while True:
        user_input = input("\nВведите выражение (число операция число) или команду: ").strip()
        if user_input.lower() == "exit":
            print("До свидания!")
            break
        elif user_input.lower() == "clear":
            clear_log()
            continue

        # парсим ввод: ожидаем три части: число, оператор, число
        parts = user_input.split()
        if len(parts) != 3:
            print("Ошибка: введите два числа и операцию через пробел. Например: 10 + 5")
            continue

        num1_str, op, num2_str = parts
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Ошибка: введите корректные числа.")
            continue

        # выполняем операцию
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Ошибка: деление на ноль невозможно.")
                continue
            result = num1 / num2
        else:
            print("Ошибка: поддерживаются операции +, -, *, /")
            continue

        expression = f"{num1} {op} {num2}"
        print(f"Результат: {result}")
        log_operation(expression, result)

if __name__ == "__main__":
    calculate()