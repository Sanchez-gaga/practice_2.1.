lines = [
    "Это первая строка текста.",
    "Вторая строка XD.",
    "Третья строка с более длинными словами и символами :)",
    "Коротко, но ясно.",
    "Пятая строка — финальная."
]

with open("text.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

with open("text.txt", "r", encoding="utf-8") as f:
    content = f.readlines()

num_lines = len(content)

all_words = []
for line in content:
    
    words = line.strip().split()
    all_words.extend(words)

num_words = len(all_words)

longest_line = max(content, key=lambda s: len(s.rstrip("\n")))

Просьба = input("Хотите увидеть? (да/нет): ")

if Просьба in {"да", "д", "yes", "y"}:
            print("\nКоличество линий:", num_lines)
            print("Количество слов:", num_words)
            print("Самая длинная строка:", longest_line.rstrip("\n"))
elif Просьба in {"нет", "н", "no", "n"}:
            print("\nЗавершение работы.")

else:
       print("\nДурак?")
