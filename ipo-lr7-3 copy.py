import json

with open("file.json", "r", encoding="utf-8") as a:
    file = json.load(a)

brik = 0
while brik < 1:
    print("""==================================
1 - Вывести все записи
2 - Вывести запись по ключу
3 - Добавить запись
4 - Удалить запись по ключу
5 - Выйти из программы
==================================""")
    
    user_input = int(input("Вы ввели: "))
    print("==================================")
#вывод информации по зна
    if user_input == 1:
        for i in file:
            print(i)

    elif user_input == 2:
        id_input = input("Введите ключ: ")
        found = False
        for i in file:
            if id_input in i.get("id", ""):  
                print(i)
                found = True
                break
        if not found:
            print("Такой записи нет :(")

    elif user_input == 3:
        add_input = input("Введите ключ для добавления: ")
        if any(add_input == i.get("id") for i in file):  
            print("Такой ключ уже есть")
        else:
            add_name_input = input("Введите название машины: ")
            add_creator_input = input("Введите название производителя: ")
            add_bool_input = input("Заправляется ли машина бензином (да/нет): ")
            add_cub_input = input("Введите объём бака в литрах: ")

            repository = {
                "id": add_input,
                "auto_name": {
                    "name": add_name_input,
                    "manufacturer": add_creator_input,
                    "is_petrol": True if add_bool_input == "да" else False,
                    "tank_volume": add_cub_input,
                }
            }
            file.append(repository)
            with open("file.json", "w", encoding="utf-8") as b:
                json.dump(file, b)  

    elif user_input == 4:
        del_input = input("Введите ключ для удаления: ")
        try:
            file.remove(next(i for i in file if del_input == i.get("id")))  
            with open("file.json", "w", encoding="utf-8") as b:
                json.dump(file, b)
        except StopIteration:
            print("Такой записи нет")

    elif user_input == 5:
        brik += 1
