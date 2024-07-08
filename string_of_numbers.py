array_of_numbers = []
string = input().split()
for number in string:
    array_of_numbers.append(int(number))
print(max(array_of_numbers),min(array_of_numbers))

