# У вас есть две группы людей.
# В одной группе состоят всеядные люди в другой лишь вегетарианцы.
# Всеядный является вегетарианцем но вегетарианец не является всеядным.
# Вывести список гостей которые могут есть овощи и зелень.

vegetarian = ["Mac DeMarco", "Franchesko Papa", "Vasya Pupkin"]
all_eat = ["Clarc Pupenberg", "Petya Pyatochkin", "Peter Griffin"]

result = []
result.extend(all_eat)
result.extend(vegetarian)
print(result)
