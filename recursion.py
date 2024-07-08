number_array = [13,2,99,4,5,66,354,167]
def recursion_sum(number_array, i=len(number_array)-1):
    if i == 0:
        return number_array[0]
    else:
        return number_array[i] + recursion_sum(number_array,i-1)
print(recursion_sum(number_array))
    