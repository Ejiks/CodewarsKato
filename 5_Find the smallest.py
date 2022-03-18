def smallest(n):
    res =[]
    if int(str(n)[1:]) == 0:
        res.append(int(str(n)[0]))
        res.append(0)
        res.append(len(str(n))-1)
        return res
    elif str(n)[1] != "0":
        x = sorted(str(n))
        z = list(str(n)).index(x[0])
        if str(n)[z] == "0":
            res.append(int(f'{str(n)[0:z]}{str(n)[z+1:]}'))
            res.append(z)
            res.append(0)
        else:
            res.append(int(f'{str(n)[z]}{str(n)[0:z]}{str(n)[z+1:]}'))
            res.append(z)
            res.append(0)
        return res
    for i in range(len(str(n))-2):
        if str(n)[i+1] == "0" and str(n)[i+2] != "0":
            res.append(int(f'{str(n)[0]}{str(n)[i+2:]}'))
            res.append(0)
            res.append(i+1)
            return res
    
    


print(smallest(285365))