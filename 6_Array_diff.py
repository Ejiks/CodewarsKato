def array_diff(a, b):
    for i in b:
        if i in a:
            for x in range(a.count(i)):
                a.remove(i)
                print(i)
    return a


print(array_diff([1,2,2], [2]))