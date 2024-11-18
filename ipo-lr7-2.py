import json
import codecs
user_input = str(input("Введите номер: "))
a = open("dump.json", encoding = "utf-8")
file = json.load(a)
find_prof = []
brik = 0
for i in file:
    if i.get("model") == "data.specialty":
        if user_input in i.get("fields").get("code"):
            brik = 1
            code = i["fields"].get("code")
            title = i["fields"].get("title")
            find_prof.append(code + " >> " + "Специальность " + title)
    elif brik != 1 and i.get("model") == "data.skill":
        if user_input in i.get("fields").get("code"):
            code = i["fields"].get("code")
            title = i["fields"].get("title")
            find_prof.append(code + " >> " + "Квалификация " + title)
    

if len(find_prof) > 0:
    print("=============== Найдено ===============")
    for i in find_prof:
        print(i)
else:
    print("=============== Не найдено ===============")
