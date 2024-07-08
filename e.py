
mn = 10**10
for n in range(4, 1000):
    s = format(n, 'b')
    if n%3==0:
        s = s + s[-3] + s[-2] + s[-1]
    else:
        s = s + format((n%3)*3, 'b')

    r = int(s, 2)
    if r > 151:
        mn = min(r, mn)

print(mn)


