def front3(str):
    if len(str) < 3:
        return str + str + str
    return str[:3] + str[:3] + str[:3]

print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))