# [ <expression> for x in <sequence> if <condition>]

data = [2,3,5,7,11,13,17,19,23,29,31]

# Updating same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# creating list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# with if condition
forx = [x for x in new_data if x%4 == 0]
print("Divisible by four: ", forx)

# using range
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)
