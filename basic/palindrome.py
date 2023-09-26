l=input()
setl=list(set(l))
c = 0
for i in setl:
    if l.count(i)%2 == 1:
        c = c + 1
if c <= 1:
    print("Yes")
else:
    print("Not")