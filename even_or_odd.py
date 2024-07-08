def even_or_odd(given_number):
    if given_number % 2 == 0:
        return "Even"
    else:
        return "Odd"

my_number = input("Enter your number here, please: ")
print(even_or_odd(my_number))