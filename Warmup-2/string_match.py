def string_match(a, b):
    count = 0
    for i in range(min(len(a), len(b)) - 1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count += 1
    return count

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))