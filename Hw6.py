import re

with open("names.txt", "w", encoding="utf-8") as file:
    file.write(f"Привет!")
with open("email.txt", "w", encoding="utf-8") as file:
    file.write(f"Добро пожаловать!")
with open("files.txt", "w", encoding="utf-8") as file:
    file.write(f"Как дела!\n")
with open("colors.txt", "w", encoding="utf-8") as file:
    file.write(f"Привет 2")

while True:
    print("1 - Считать имена и фамилии.\n"
          "2 - Считать все емайлы.\n"
          "3 - Считать названия файлов.\n"
          "4 - Считать цвета.\n"
          "5 - Выход")
    user = int(input("Что вы хотите считать: "))
    if user == 5:
        print("Я устал иду спать.")
        break
    elif user == 1:
        print("\nИдет сортировка имен и фамилий")
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as file:
            content_names = file.read()
            names = re.findall(r"(\b[A-Z|O\'].[A-z|A-z\-a-z|A-z A-z]{1,}[^A-Za-z\.a-z])", content_names)
            # names = re.findall(r"[A-Z]+[A-z]+\w+\s+[A-z]+[a-z]+\w+|[A-Z]+[A-z]+\w+\s+[A-Z][']\s+[A-z]+[a-z]+\w+",content_names)

            for i in range(len(names)):
                if not i % 2:
                    with open("names.txt", "a", encoding="utf-8") as file:
                        file.write(f"Имя: {names[i]} ")
                else:
                    with open("names.txt", "a", encoding="utf-8") as file:
                        file.write(f"Фамилия:{names[i]}\n")
    elif user == 2:
        print("\nИдет сортировка почты")
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as file:
            content_emails = file.read()
            emails = re.findall(r"[a-z|a-z0-9]{0,}[@][a-z]{0,}[\.a-z]{0,}", content_emails)

            for i in emails:
                with open("email.txt", "a", encoding="utf-8") as file:
                    file.write(f"Почта: {i}\n")
    elif user == 3:
        print("\nИдет сортировка файлов")
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as file:
            content_files = file.read()
            files = re.findall(r"[A-Z][A-z]{0,}\.[a-z|mp3]{1,}", content_files)

            for i in files:
                with open("files.txt", "a", encoding="utf-8") as file:
                    file.write(f"Файл: {i}\n")
    elif user == 4:
        print("\nИдет сортировка цветов")
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as file:
            content_colors = file.read()
            colors = re.findall(r"#[a-z0-9]{6}", content_colors)

            for i in colors:
                with open("colors.txt", "a", encoding="utf-8") as file:
                    file.write(f"Цвет: {i}\n")
    else:
        print("1 - Считать имена и фамилии.\n"
              "2 - Считать все емайлы.\n"
              "3 - Считать названия файлов.\n"
              "4 - Считать цвета.\n"
              "5 - Выход")