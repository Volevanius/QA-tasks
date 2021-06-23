# У вас есть группа людей с неуникальными именами.
# Сформируйте список не повторяющихся имен (для этой задачи нельзя использовать set.
# Если в списке есть 2 джона нужно взять лишь одного из них.
# "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow")

people_list = [
    "John Dow",
    "Marta Stuard",
    "Clarc Pupenberg",
    "Petya Pyatochkin",
    "Peter Griffin",
    "Mac DeMarco",
    "Franchesko Papa",
    "Vasya Pupkin",
    "Peter Griffin",
    "Marta Stuard"
]

people_list_dict = {}
for name in people_list:
    people_list_dict.setdefault(name, None)

people_list_dedup = list(people_list_dict.keys())
print(people_list_dedup)
