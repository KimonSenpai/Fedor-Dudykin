f = open("24.txt", "r")

s = f.readline()
c = 0

for i in range(len(s) - 5):
    if s[i:i+5] == "OKTOS":
        c+=1
print(c)