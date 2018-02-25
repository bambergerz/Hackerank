from mean_median_mode import median


sample_input = "3 7 8 5 12 14 21 13 18"

# num_items = int(input())
# a = list(map(int, input().split(" ")))
# list.sort(a)


def partition(a):
    l = len(a)
    lower = a[0:(l // 2)]
    if l % 2 == 0:
        upper = a[(l//2):]
    else:
        upper = a[(l//2 + 1):]
    return lower, upper


def quartile(n, a):
    list.sort(a)
    if n == 2:
        return median(a)
    else:
        lower, upper = partition(a)
        if n == 1:
            return median(lower)
        elif n == 3:
            return median(upper)
        else:
            raise AssertionError("Invalid entry for value n: " + str(n))

# print(quartile(1, a))
# print(quartile(2, a))
# print(quartile(3, a))