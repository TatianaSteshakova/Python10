pets = dict()
n = int(input("Введите кол-во питомцев: "))

for i in range (0, n):
    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца питомца: ")
    pets[name] = {
        "Вид питомца": pet_type,
        "Возраст": age,
        "Имя владельца": owner_name
    }


for k, v in pets.items():
    str_age = ""
    age = v["Возраст"]
    if age % 10 == 1 and age % 100 != 11:
        str_age = f"{age} год"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        str_age = f"{age} года"
    else:
        str_age = f"{age} лет"
    print("Это", v["Вид питомца"], "по кличке", k + ".", "Возраст питомца:", str_age + ".","Имя владельца:", v["Имя владельца"])
