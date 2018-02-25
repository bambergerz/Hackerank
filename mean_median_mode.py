import sys

# num_items = int(input())
# a = list(map(int, input().split(" ")))


def mean(a):
    my_sum = 0
    for x in a:
        my_sum += x
    return round(my_sum / len(a), 1)


def median(a):
    list.sort(a)
    l = len(a)
    if l % 2 == 0:
        return round((a[l // 2 - 1] + a[l // 2]) / 2, 2)
    else:
        return round(a[l // 2], 2)


def mode(a):
    counters = {}
    for x in a:
        if x in counters.keys():
            counters[x] += 1
        else:
            counters[x] = 1
    max_counter = 0
    item = sys.maxsize
    for key, value in counters.items():
        if value > max_counter:
            max_counter = value
            item = key
        elif value == max_counter:
            if key < item:
                item = key
        else:
            pass
    return item


# print(mean(a))
# print(median(a))
# print(mode(a))
