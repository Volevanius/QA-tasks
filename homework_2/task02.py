# У вас есть 3 группы людей bigno_blacklist, poker_blacklist, majong_blacklist.
# Имена людей в формате "John Dow" первое и второе имя.
# Найти тех кто состоит во всех черных списках.

bigno_blacklist = {"Mac DeMarco", "Franchesko Papa", "Vasya Pupkin"}
poker_blacklist = {"Clarc Pupenberg", "Petya Pyatochkin", "Mac DeMarco", "Franchesko Papa"}
majong_blacklist = {"PVasya Pupkin", "Mac DeMarco", "Franchesko Papa"}

totally_banned = bigno_blacklist.intersection(poker_blacklist).intersection(majong_blacklist)
print(totally_banned)
