#Задача 4.7

mac = "AAAA:BBBB:CCCC"
macstr = mac.replace(':', '')
res = ''.join(format(i, '08b') for i in bytearray(macstr, encoding='utf-8'))
print(res)
