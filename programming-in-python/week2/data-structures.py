# Lists

list = ["hello partner", 29, 0.3, False]

list2 = ["A", "B", "C"]

# print(*list)
# print(list2, sep=", ")

list.insert(2, "NO")
list.append(True)
list.pop()

#Tuples

my_tuple = (1,2,3,4,5)
my_tuple2 = (1, "Hello", False)

# print(my_tuple2.count("Hello"))
# print(my_tuple.index(4))

#Sets

set_a = {1,2,3,4}
set_a.add(5)
set_a.remove(2)

# print(set_a)

#Dictionaries

my_d = {1: "Test", "Name": "Jox"}

# print(my_d["Name"])

# for key, value in my_d.items():
#     print(key, ": ", value)


# Kwargs and args

# def sum_of(*args):
#     sum = 0
#     for x in args:
#         sum+= x
#     return sum

def sum_of(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_of(coffe= 2.99, cake=4.55, juice=2.99))