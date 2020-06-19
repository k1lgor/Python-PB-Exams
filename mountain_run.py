import math

rec_in_sec = float(input())
dist_in_m = float(input())
sec_for_one_m = float(input())
dist_in_sec = dist_in_m * sec_for_one_m
delay = math.floor(dist_in_m / 50) * 30
ttl_dist_in_sec = dist_in_sec + delay
dif = abs(ttl_dist_in_sec - rec_in_sec)
if ttl_dist_in_sec < rec_in_sec:
    print(f'Yes! The new record is {ttl_dist_in_sec:.2f} seconds.')
else:
    print(f'No! He was {dif:.2f} seconds slower.')
