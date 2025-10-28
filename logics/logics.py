#Two sum

num = [7,0,2,4,1,7,3,9,12]
target = 12
listt = []
seen = set()

for i in num:
    compl = target - i
    if compl in seen:
        listt.append((compl,i))
    seen.add(i)

print(listt)