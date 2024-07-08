import random
numbers = ['1','2','3','4','5','6','7','8','9','0']
big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
password_len = int(input())
password_template = ''
for i in range(password_len):
    password_template = password_template + str(random.randint(1,4))
password =''
for number in password_template:
    if number == '1':
        password = password + numbers[random.randint(0,len(numbers)-1)]
    if number == '2':
        password = password + big_letters[random.randint(0,len(big_letters)-1)]
    if number == '3':
        password = password + small_letters[random.randint(0,len(small_letters)-1)]
    if number == '4':
        password = password + symbols[random.randint(0,len(symbols)-1)]
print(password)
    