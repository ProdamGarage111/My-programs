def square_digits(given_number):
    final_number = ''
    for character in given_number:
        final_number = final_number + str(int(character)**2)
    
    return final_number