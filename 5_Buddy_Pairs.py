def buddy(start, limit):
    for z in range(start, limit+1):
        sum_n = 0
        sum_m = 0
        for i in range(z - 1, 0, -1):
            if (z % i == 0):
                sum_n += i
        for x in range(sum_n - 2, 0, -1):
            if ((sum_n-1) % x == 0):
                sum_m += x
        if z+1 == sum_m:
            return [z, sum_n-1]
    return "Nothing"

print(buddy(10, 13))