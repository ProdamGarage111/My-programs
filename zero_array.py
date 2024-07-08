array = [1, 0, 1, 2, 0, 1, 3]
for i in array:
    if i == 0:
        array.remove(i)
        array.append(i)
print(array)
