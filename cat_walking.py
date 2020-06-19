min_per_day = int(input())
walks_per_day = int(input())
cal_per_day = int(input())
ttl_mins = min_per_day * walks_per_day
ttl_cal = ttl_mins * 5
half = cal_per_day * 50 / 100
if ttl_cal >= half:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {ttl_cal}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {ttl_cal}.')
