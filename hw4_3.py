def process_file(new_text, file_name):

    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(new_text + '\n')
    print("Строка добавлена\n")

    with open(file_name, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()
        print(f"Всего строк: {len(all_lines)}")
        print("Четные строки:")
        for num, line in enumerate(all_lines):
            if num % 2 == 1:
                print(f"  {num + 1}: {line.strip()}")

print("Начинаем работу с файлом")

with open("data.txt", 'w', encoding='utf-8') as f:
    f.write("Раз\n")
    f.write("Два\n")
    f.write("Три\n")
    f.write("Четыре\n")
print("Начальные строки записаны\n")

process_file("Пять", "data.txt")
print()
process_file("Шесть", "data.txt")
print()
process_file("Семь", "data.txt")
