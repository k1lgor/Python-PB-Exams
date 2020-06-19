pens = int(input())
markers = int(input())
deter = float(input())
disc = int(input())
ttlpens = pens * 5.8
ttlmarkers = markers * 7.2
ttldeter = deter * 1.2
sum = ttlpens + ttlmarkers + ttldeter
sumdisc = sum - sum * disc / 100
print(f'{sumdisc:.3f}')