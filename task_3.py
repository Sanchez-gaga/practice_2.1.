import csv
import os

FILENAME = 'products.csv'

def initialize_file():
    if not os.path.exists(FILENAME):
        initial_data = [
            ['Название', 'Цена', 'Количество'],
            ['Яблоки', 100, 50],
            ['Бананы', 80, 30],
            ['Молоко', 120, 20],
            ['Хлеб', 40, 100]
        ]
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(initial_data)
        print(f"Файл {FILENAME} создан с начальными данными.")

def load_products():
    products = []
    try:
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                
                row['Цена'] = float(row['Цена'])
                row['Количество'] = int(row['Количество'])
                products.append(row)
    except FileNotFoundError:
        print("Файл не найден.")
    return products

def save_products(products):
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Название', 'Цена', 'Количество']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)
    print("Данные успешно сохранены.")

def add_product(products):
    name = input("Введите название товара: ")
    try:
        price = float(input("Введите цену: "))
        quantity = int(input("Введите количество: "))
        products.append({'Название': name, 'Цена': price, 'Количество': quantity})
        print("Товар добавлен.")
    except ValueError:
        print("Ошибка: Цена и количество должны быть числами!")

def search_product(products):
    search_name = input("Введите название товара для поиска: ").lower()
    found = False
    for item in products:
        if item['Название'].lower() == search_name:
            print(f"Найдено: {item['Название']} | Цена: {item['Цена']} | Кол-во: {item['Количество']}")
            found = True
    if not found:
        print("Товар не найден.")

def calculate_total_value(products):
    total = sum(item['Цена'] * item['Количество'] for item in products)
    print(f"Общая стоимость всех товаров на складе: {total:.2f}")

def main():
    initialize_file()
    products = load_products()

    while True:
        print("\n-- Меню управления складом --")
        print("1. Показать все товары")
        print("2. Добавить новый товар")
        print("3. Поиск товара по названию")
        print("4. Рассчитать общую стоимость склада")
        print("5. Сохранить изменения")
        print("0. Выход")
        
        choice = input("Выберите действие: ")

        if choice == '1':
            print("\nСписок доступных товаров:")
            for p in products:
                print(f"{p['Название']}: {p['Цена']} руб., {p['Количество']} шт.")
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            search_product(products)
        elif choice == '4':
            calculate_total_value(products)
        elif choice == '5':
            save_products(products)
        elif choice == '0':
            
            save_confirm = input("Сохранить изменения перед выходом? (да/нет): ")
            if save_confirm.lower() == 'да':
                save_products(products)
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()