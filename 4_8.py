#Задача 4.8

ip = "192.168.3.1"
octa = []
for i in ip.split('.'):
    octa.append(int(i))
printer = '''
    IP address:
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}'''
print(printer.format(*octa))

