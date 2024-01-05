def makes10(a, b):
    if a + b is 10 or a is 10 or b is 10:
        return True
    return False

print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))