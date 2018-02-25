from quartiles import quartile


num_items = int(input())
a = list(map(int, input().split(" ")))
f = list(map(int, input().split(" ")))



def expand(a, f):
    assert len(a) == len(f), "The length of 'a' (" + str(len(a)) + ") and 'f' ( " + str(len(f)) + " ) are not equal"
    total = []
    for x in range(len(a)):
        for freq in range(f[x]):
            total.append(a[x])
    list.sort(total)
    return total


def interquantile_range(a):
    return round(float(quartile(3, a) - quartile(1, a)), 1)


if __name__ == "__main__":
    expanded = expand(a, f)
    print(interquantile_range(expand(a, f)))
