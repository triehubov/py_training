#Задача 4.3

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = config.split()[4]
result = result.split(',')
print(result)
print(type(result))
