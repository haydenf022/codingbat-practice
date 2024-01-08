def parrot_trouble(talking, hour):
    if talking is True and (hour < 7 or hour > 20):
        return True
    return False

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))