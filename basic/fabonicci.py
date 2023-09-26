r=8
c=[0,1]
# for i in range(r):
#     print(c[-1])
#     c.append(c[-1]+c[-2])

def fabb( r, c):
    if r:
        c.append(c[-1]+c[-2])
        fabb( r-1, c)
fabb(r,c)
print(c)