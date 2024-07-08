k = 0
for x1 in "234567":
    for x2 in "0234567":
        for x3 in "0234567":
             for x4 in "0234567":
                  for x5 in "0234567":
                    our_number = x1+x2+x3+x4+x5
                    if our_number.count(x1)==1 and our_number.count(x2)==1 and our_number.count(x3)==1 and our_number.count(x4)==1 and our_number.count(x5)==1:
                        if x1 in '0246' and x2 in '1357' and x3 in '0246' and x4 in '1357' and x5 in '0246':
                            k=k+1
                            print(our_number)
                        if x1 in '1357' and x2 in '0246' and x3 in '1357' and x4 in '0246' and x5 in '1357':
                            k=k+1  
                            print(our_number)
print(k)




