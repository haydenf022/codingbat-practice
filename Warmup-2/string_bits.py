def string_bits(str):
    final = ''
    for n in range(0, len(str)):
        if n % 2 == 0:
            final += str[n]
    return final

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))