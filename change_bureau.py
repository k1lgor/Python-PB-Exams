oneBT = 1168
oneYuan = 0.15
usd = 1.76
euro = 1.95
bitcoins = int(input())
yuans = float(input())
comm = float(input())
BT = oneBT * bitcoins
Y = yuans * oneYuan * usd
ttl = (BT + Y) / euro
com = ttl * comm / 100
sum = ttl - com
print(f'{sum:.2f}')