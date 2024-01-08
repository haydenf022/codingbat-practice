def string_splosion(str):
    answer = ''
    for n in range(0, len(str)):
        answer += str[:n]
    return answer + str
        

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))