num_elements = int(input())
nums = list(map(int, input().split(" ")))
weights = list(map(int, input().split(" ")))


def weighted_mean(a, w):
    l = len(a)
    num = 0
    den = 0
    for x in range(l):
        num += a[x] * w[x]
        den += w[x]
    return round(num / den, 1)


print(weighted_mean(nums, weights))
