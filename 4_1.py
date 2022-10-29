#Задача 4.1

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat = nat.replace('Fast', 'Giga')
print(nat)
