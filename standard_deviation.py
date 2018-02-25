import sys
from mean_median_mode import mean


num_items = int(input())
a = list(map(int, input().split(" ")))


def standard_dev(a):
    a_mean = mean(a)
    total = 0
    for x in a:
        total += pow(x - a_mean, 2)
    return round(pow(total / num_items, 0.5), 1)


print(standard_dev(a))