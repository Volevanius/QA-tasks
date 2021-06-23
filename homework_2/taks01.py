# У вас есть 2 компании с людьми.
# Одна из компаний пусть будет это global_logic была поглощена компанией toshiba.
# Отобразите это в коде.
# Учитывайте что люди с одинаковыми именами могут быть в обеих компаниях.

global_logic = ["Mac DeMarco", "Franchesko Papa", "Vasya Pupkin"]
toshiba = ["Clarc Pupenberg", "Petya pyatochkin", "Mac DeMarco"]

toshiba.extend(global_logic)
print(toshiba)
