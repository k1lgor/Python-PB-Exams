fruit = str(input())
set = str(input())
order_set = int(input())
a = 0.0
if fruit == 'Watermelon':
    if set == 'small':
        a = order_set * 2 * 56
    else:
        a = order_set * 5 * 28.7
elif fruit == 'Mango':
    if set == 'small':
        a = order_set * 2 * 36.66
    else:
        a = order_set * 5 * 19.6
elif fruit == 'Pineapple':
    if set == 'small':
        a = order_set * 2 * 42.1
    else:
        a = order_set * 5 * 24.8
elif fruit == 'Raspberry':
    if set == 'small':
        a = order_set * 2 * 20
    else:
        a = order_set * 5 * 15.2
if a > 1000:
    a *= 0.5
    print(f'{a:.2f} lv.')
elif 400 <= a <= 1000:
    a *= 0.85
    print(f'{a:.2f} lv.')
else:
    print(f'{a:.2f} lv.')