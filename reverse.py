my_sentence = input().split()
for i in range (len(my_sentence)):
    if len(my_sentence[i]) > 5:
        my_sentence[i] = my_sentence[i][::-1]
my_sentence = ' '.join(my_sentence)
print(my_sentence)
       
