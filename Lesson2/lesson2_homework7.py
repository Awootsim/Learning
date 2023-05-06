
string1 = "omg"
string2 = "abcdefghjklmnoqrstuxyz"
a = string2.find(string1[0])
b = string2.find(string1[1])
c = string2.find(string1[2])
end = max(a, b, c)
start = min(a, b, c)
print(string2[start:end+1])
