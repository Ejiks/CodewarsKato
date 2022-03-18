def make_readable(seconds):
    hh = seconds//(60**2)
    if len(str(hh)) != 2:
        hh = f"0{hh}"
    mm = seconds//(60)-hh*60
    if len(str(mm)) != 2:
        mm = f"0{mm}"
    ss = seconds - mm*60 - hh*60*60
    if len(str(ss)) != 2:
        ss = f"0{ss}"

    
    return f'{hh}:{mm}:{ss}'


print(make_readable(60))