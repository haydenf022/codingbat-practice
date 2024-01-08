def front_times(str, n):
    answer = ''
    if len(str) >= 3:
        front = str[:3]
    else:
        front = str
    for i in range(0, n):
        answer += front
    return answer
    

print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))