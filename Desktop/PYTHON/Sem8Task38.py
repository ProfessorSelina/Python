# "1: Просмотр всех записей справочника\n" +
# "2: Добавление новой записи\n"+
# "3: Поиск по справочнику\n"+
# "4: Изменение строки справочника\n"+
# "5: Удаление записи из справочника\n"+
# "6: Выход\n**********************")



import csv

def display_all_records():
    for row in reader:
        print(f"Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n")


def find_last_name(reader):
    last_name = input("Введите фамилию: ")
    for elem in filter(lambda x: x[0] == last_name, reader):
        print(f"Фамилия: {elem[0]}\nИмя: {elem[1]}\nНомер телефона: {elem[2]}\nКомментарий: {elem[3]}\n")


def find_phone_number(reader):
    phone = input("Введите номер телефона: ")
    for elem in filter(lambda x: x[2] == phone, reader):
        print(f"Фамилия: {elem[0]}\nИмя: {elem[1]}\nНомер телефона: {elem[2]}\nКомментарий: {elem[3]}\n")

def add_abonent():
    with open('phonebook.csv', "a", encoding="utf-8", newline="") as out_file:
        info = input("Введите данные абонента через запятую: ").split(", ")
        csv.writer(out_file).writerow(info)
        print(f"Данные абонента {info[1]} {info[0]} записаны")

def del_abonent():
    with open('phonebook.csv', "r+", encoding="utf-8",) as del_file:
        info = input("Введите фамилию и номер телефона абонента для удаления (через запятую): ").split(", ")
        data = list(csv.reader(del_file))
        user_info = list(filter(lambda x: x[0] == info[0] and x[2] == info[1], data))
        if len(user_info) > 0:
            data.remove(user_info[0])
            del_file.seek(0)
            csv.writer(del_file).writerows(data)
            del_file.truncate()
            print(f"Пользователь с фамилией {info[0]} и телефоном {info[1]} удален.")
        else:
            print(f"Пользователь с фамилией {info[0]} и телефоном {info[1]} не найден.")

def change_user_info():
    with open('phonebook.csv', "r+", encoding="utf-8",) as change_file:
        info = input("Введите фамилию и номер телефона абонента для изменения (через запятую): ").split(", ")
        data = list(csv.reader(change_file))
        user_info = list(filter(lambda x: x[0] == info[0] and x[2] == info[1], data))
        if len(user_info) > 0:
            new_user_info = input("Обновленные данные пользователя "
                                  "(Фамилия, имя, телефон и комментарий через запятую): ").split(", ")
            data.remove(user_info[0])
            file.seek(0)
            writer = csv.writer(change_file)
            writer.writerows(data)
            writer.writerow(new_user_info)
            print("Данные пользователя изменены")
        else:
            print(f"Пользователь с фамилией {info[0]} и телефоном {info[1]} не найден.")

for elem in iter(input, "7"):
    with open('phonebook.csv', "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        if elem == "1":
            display_all_records()

        elif elem == "2":
            find_last_name(reader)

        elif elem == "3":
            find_phone_number(reader)

        elif elem == "4":
            add_abonent()

        elif elem == "5":
            del_abonent()

        elif elem == "6":
            change_user_info()


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(' ')))
            data.append(record)

    return data