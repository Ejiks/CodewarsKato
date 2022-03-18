def nickname_generator(name):
    if len(name) <= 3:
        return "Error: Name too short"
    elif name[2] in "aeiou":
        return name[0:4]
    else:
        return name[0:3]

print(nickname_generator("Samantha"))