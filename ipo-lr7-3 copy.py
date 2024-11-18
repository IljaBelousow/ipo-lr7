import json
a = open("file.json", encoding = "utf-8")
file = json.load(a)
brik = 0
b_bool = False
while brik < 1:
    print("""==================================
1 - Вывести все записи
2 - Вывести запись по полю
3 - Добавить запись
4 - Удалить запись по полю
5 - Выйти из программы
=================================="""
    )
    user_input = int(input("Вы ввели: "))
    print("==================================")

    if user_input == 1:
        for i in file:
            print(i)

    elif user_input == 2:
        id_input = input("Введите ключ: ")
        index = False
        for i in file:
            if id_input in i:
                print(i)
                found = True
                break
        if not index:
                print("Такой записи нет :(")

    elif user_input == 3:
        add_input = input("Введите ключ для добавления: ")
        for i in file:
            if add_input in i:
                print("==================================")
                print("Такой ключ уже существует")
                break
            else:
                add_name_input = input("Введите название машины: ")
                add_creator_input = input("Введите название производителя: ")
                add_bool_input = input("Запрявляется ли машина бензином да/нет: ")
                if add_bool_input == "да":
                    b_bool = True;
                add_cub_input = input("Введите объём бака в литрах: ")
                repository = {
        add_input: {
            "name": add_name_input,
            "manufacturer": add_creator_input,
            "is_petrol": add_bool_input,
            "tank_volume": add_cub_input,
        }
    }
                file.append(repository)
                b = open("file.json", "w", encoding="utf-8")
                json.dump(file, b)

    elif user_input == 4:
        del_input = input("Введите ключ для удаления: ")
        for i in file:
            if del_input in i:
                file.remove(i)
            else:
                print("Такой записи нет :(")
        with open("file.json", "w", encoding="utf-8") as b:
            json.dump(file, b)

    elif user_input == 5:
        brik += 1