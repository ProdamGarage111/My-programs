my_array = [1,2,2,3,3,3,4,3,3,3,2,2,1]
for i in my_array:
    a = my_array.count(i)
    if a % 2 != 0:
        print(i)

