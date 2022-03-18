import itertools

def permutations(string):
    x = list(itertools.product(string, repeat=len(string)))
    res = []
    for i in x:
        z = "".join(i)
        if sorted(list(z)) == sorted(list(string)):
            res.append(z)
    return list(set(res))

print (permutations("1234"))

print(set(itertools.permutations("abba")))
# s = "123456"
# print(s.replace(s[2], s[1]))




# iter = 0
#         for w in range(len(z)):
#             if z.count(z[w]) == string.count(z[w]):
#                 iter += 1
#                 if iter == len(z):