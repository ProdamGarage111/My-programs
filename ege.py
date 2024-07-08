
for n in range(100, 1000):
    my_string = '5' +'2'*n
    while '52' in my_string or '2222' in my_string or '1122' in my_string:
        if '52' in my_string:
           my_string = my_string.replace('52','11',1) 
        if '2222' in my_string:
            my_string = my_string.replace('2222','5',1)
        if '1122' in my_string:
            my_string = my_string.replace('1122','25',1)
    s = 0
    for character in my_string:
        s = s + int(character)
    if s == 64:
        print(n)
        
        
