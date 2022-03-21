def make_readable(seconds):
    ss = 0
    mm = 0
    hh = 0
    for i in range(seconds):
        if ss <59:
            ss +=1
        else:
            if mm <59:
                mm +=1
                ss =0
            else:
                hh +=1
                mm =0
                ss =0
    return f'{hh:02}:{mm:02}:{ss:02}'


print(make_readable(359999))