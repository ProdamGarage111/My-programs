Summ = 0
n = int(input())
for i in range(1,n):
    if i % 3 == 0 or i % 5 == 0:
        Summ += i
        print(i)
print(Summ)  