def last2(str):
    count = 0
    last = str[len(str) - 2 : len(str)]
    for n in range(0, len(str) - 2):
        if str[n] + str[n + 1] == last:
            count += 1
    return count

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))