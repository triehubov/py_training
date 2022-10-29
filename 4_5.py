#Задача 4.5

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
result1 = command1.split()[4]
result1 = result1.split(',')
command2 = "switchport trunk allowed vlan 1,3,8,9"
result2 = command2.split()[4]
result2 = result2.split(',')

uresult = result1 + result2
result = list({x for x in uresult if uresult.count(x) > 1})
print(result)
