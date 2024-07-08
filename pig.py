my_string ="Hello world !".split()
transformed_string = []
for word in my_string:
    if word.isalpha():
        transformed_word = word[1:] + word[0] + "ay"
    else:
        transformed_word = word
    transformed_string.append(transformed_word)

transformed_string = ' '.join(transformed_string)
print(transformed_string)
    