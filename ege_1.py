for x in "0123456789ABCDEFGHI":
    a = int('98897'+ x +'21',19)
    a += int('2'+ x +'923',19)
    if a %18==0:
        print(x,a//18)