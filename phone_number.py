phone_number = map(str,[1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
phone_number = "".join(phone_number)
print("(" + phone_number[0:3] + ")" + phone_number[3:6] +"-" + phone_number[6:10])