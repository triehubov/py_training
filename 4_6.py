# Задача 4.6
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
list1 = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
list2 = ospf_route.split()
list3 = ''
i = 0
while i < len(list1):
    list3 += list1[i]+' '+list2[i]+'\n'
    i += 1

print(list3)
