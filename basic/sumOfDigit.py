
def sum(n):
    if n<10:
        return n
    return sum(n//10) + n%10
n=int(str(4855)[::-1])
print(sum(458),n)