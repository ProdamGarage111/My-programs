def plus(y): 
    return lambda x: x + y
def ret(function):
    return function(5)

print(ret(plus(7)))