my_file = open("17.txt")
array =[]
counter = 0
max_sum = 0
for line in my_file:
    array.append(int(line))
for i in range (len(array)-1):
    for j in range (i+1,len(array)):
        if (array[i]%160 != array[j]%160) and (array[i]%7==0 or array[j]%7==0):
           counter += 1
           s = array[i] + array[j]
           maximum = max(max_sum, s)
print(counter, maximum)


