array_of_vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
troll_comment = input()
processed_comment = ""
for character in troll_comment:
    if character in array_of_vowels:
        pass
    else:
        processed_comment = processed_comment + character
print(processed_comment)
