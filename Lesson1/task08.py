# 8. Создайте 2 переменные john, marta. Переменные должны быть словарями с ключами: full_name, age, salary, gender, friends, coordinates.
# Требования к структуре:
# Full_name - полное имя
# Age - возраст
# Salary - зароботная плата
# Gender - пол человека (используйте булев тип)
# Friends - список друзей из задачи 6
# Coordinates - долгота и широта из задачи 7
# Вывести в консоль джона и марту ключ и значение: “key => value” где key это ключ пары из словаря а value это значение пары из словаря.

john = {
    'Full_name': "John",
    'Age': 25,
    'Salary': 1500.5,
    'Gender': True,
    'Friends': ["Vanya", "Sanya", "Vitalya"],
    'Coordinates': (50.447254, 30.5212699)
}
marta = {
    'Full_name': "Marta",
    'Age': 48,
    'Salary': 2000.1,
    'Gender': False,
    'Friends': ["Svetik", "Nedenka", "Taniusha"],
    'Coordinates': (52.412331, 28.5235325)
}

for key, value in john.items():
    print(f"{key}  => {value}")
print("------------------------")
for key, value in marta.items():
    print(f"{key}  => {value}")
