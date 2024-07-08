input_character = 55
my_array = []
total_sum = 0
while input_character != '!':
    input_character = input()
    if input_character != '!':
        my_array.append(input_character)
my_array = list(map(int, my_array))
for i in my_array:
    if i > 0:
        total_sum += i

print(total_sum)

