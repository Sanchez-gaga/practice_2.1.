import json
import os

FILENAME = 'library.json'
EXPORT_FILE = 'available_books.txt'

def load_data():
    if not os.path.exists(FILENAME):
        initial_data = [
            {
                "id": 1,
                "title": "Мастер и Маргарита",
                "author": "Булгаков",
                "year": 1967,
                "available": True
            },
            {
                "id": 2,
                "title": "Преступление и наказание",
                "author": "Достоевский",
                "year": 1866,
                "available": False
            }
        ]
        save_data(initial_data)
        return initial_data
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(books):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def view_books(books):
    print("\n--- Список всех книг ---")
    for b in books:
        status = "В наличии" if b['available'] else "Выдана"
        print(f"ID: {b['id']} | '{b['title']}' - {b['author']} ({b['year']}) [{status}]")

def search_books(books):
    query = input("Введите название или автора для поиска: ").lower()
    found = [b for b in books if query in b['title'].lower() or query in b['author'].lower()]
    if found:
        view_books(found)
    else:
        print("Книги не найдены.")

def add_book(books):
    new_id = max([b['id'] for b in books], default=0) + 1
    title = input("Название книги: ")
    author = input("Автор: ")
    try:
        year = int(input("Год издания: "))
        books.append({
            "id": new_id,
            "title": title,
            "author": author,
            "year": year,
            "available": True
        })
        save_data(books)
        print("Книга успешно добавлена!")
    except ValueError:
        print("Ошибка: Год должен быть числом.")

def change_status(books):
    try:
        book_id = int(input("Введите ID книги для смены статуса: "))
        for b in books:
            if b['id'] == book_id:
                b['available'] = not b['available']
                save_data(books)
                print(f"Статус изменен. Теперь: {'В наличии' if b['available'] else 'Выдана'}")
                return
        print("Книга с таким ID не найдена.")
    except ValueError:
        print("Ошибка: ID должен быть числом.")

def delete_book(books):
    try:
        book_id = int(input("Введите ID книги для удаления: "))
        for i, b in enumerate(books):
            if b['id'] == book_id:
                books.pop(i)
                save_data(books)
                print("Книга удалена.")
                return
        print("Книга с таким ID не найдена.")
    except ValueError:
        print("Ошибка: ID должен быть числом.")

def export_available(books):
    available_books = [b for b in books if b['available']]
    with open(EXPORT_FILE, 'w', encoding='utf-8') as f:
        for b in available_books:
            f.write(f"ID: {b['id']}, Название: {b['title']}, Автор: {b['author']}\n")
    print(f"Список доступных книг экспортирован в {EXPORT_FILE}")

def main():
    books = load_data()
    
    while True:
        print("\n--- Система учета книг ---")
        print("1. Просмотр всех книг")
        print("2. Поиск книги")
        print("3. Добавить новую книгу")
        print("4. Изменить статус (взята/возвращена)")
        print("5. Удалить книгу")
        print("6. Экспорт доступных книг в TXT")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1': view_books(books)
        elif choice == '2': search_books(books)
        elif choice == '3': add_book(books)
        elif choice == '4': change_status(books)
        elif choice == '5': delete_book(books)
        elif choice == '6': export_available(books)
        elif choice == '0': break
        else: print("Неверный выбор.")

if __name__ == "__main__":
    main()