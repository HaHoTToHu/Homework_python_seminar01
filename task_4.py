# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
choco_part_1 = int(input("Введите первую сторону шоколадки: "))
choco_part_2 = int(input("Введите вторую сторону шоколадки: "))
breaked_part = int(input("Введите часть, которую отламливаем: "))

if (breaked_part % choco_part_1 == 0 or breaked_part % choco_part_2 == 0) and (choco_part_1 * choco_part_2) >= breaked_part:
    print("Да")
else:
    print("Нет")