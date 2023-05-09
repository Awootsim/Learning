number_people = 7
kill_num = 3
s = [i for i in range(1, number_people + 1)]
while len(s) > 1:
    for q in range(0, kill_num - 1):
        s.append(s[q])
    del s[:kill_num]
survivor = s[0]
print(survivor)
