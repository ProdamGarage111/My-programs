initial_seconds= int(input())
clock_seconds = initial_seconds % 60
number_of_minutes = initial_seconds // 60
clock_minutes = number_of_minutes % 60
clock_hours = number_of_minutes // 60
print(clock_seconds,clock_minutes,clock_hours)

