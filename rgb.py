def decimal_to_hex(decimal_number):
    # Проверка на ноль
    if decimal_number == 0:
        return "0"
    
    # Словарь для перевода цифр в шестнадцатеричный формат
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""
    
    # Цикл деления с остатком
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_number = hex_digits[remainder] + hexadecimal_number
        decimal_number //= 16
    
    return hexadecimal_number
my_string=""
rgb = [255,255,255]
for number in rgb:
    my_string = my_string + str(decimal_to_hex(number)) 
print('#'+my_string)
