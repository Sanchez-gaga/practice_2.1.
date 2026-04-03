def main():
    students = []  

    try:
        with open('students.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:  
                    continue
                
                name, grades_str = line.split(':', 1)
                
                grades = list(map(int, grades_str.split(',')))
                
                avg = sum(grades) / len(grades)
                students.append((name, grades, avg))
    except FileNotFoundError:
        print("Файл students.txt не найден. Создаём файл с примером данных.")
        
        example_data = [
            "Иванов Иван:5,4,3,5",
            "Петров Петр:4,3,4,4",
            "Сидорова Мария:5,5,5,5"
        ]
        with open('students.txt', 'w', encoding='utf-8') as f:
            for line in example_data:
                f.write(line + '\n')
        
        for line in example_data:
            name, grades_str = line.split(':', 1)
            grades = list(map(int, grades_str.split(',')))
            avg = sum(grades) / len(grades)
            students.append((name, grades, avg))

    if students:
        best_student = max(students, key=lambda x: x[2])  
        print(f"Студент с наивысшим средним баллом: {best_student[0]} ({best_student[2]:.2f})")
    else:
        print("Нет данных о студентах.")
        return

    with open('result.txt', 'w', encoding='utf-8') as f:
        for name, grades, avg in students:
            if avg > 4.0:
                grades_str = ','.join(map(str, grades))
                f.write(f"{name}:{grades_str}\n")

if __name__ == "__main__":
    main()