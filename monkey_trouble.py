def monkey_trouble(a_smile, b_smile):
    if a_smile and not b_smile or b_smile and not a_smile:
        return False
    else:
        return True
    
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
    
