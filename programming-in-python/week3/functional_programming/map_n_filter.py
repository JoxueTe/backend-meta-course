menu = ["espresso", "latte", "cappuccino", "cortado", "americano"]

def find_coffe(coffe):
    if coffe[0] == 'c':
        return coffe
    
########### MAP #####################
# map_coffe = map(find_coffe, menu)
# print(map_coffe)
# for i in map_coffe:
#     print(i)

########### FILTER #################
filter_coffe = filter(find_coffe, menu)
print(filter_coffe)
for i in filter_coffe:
    print(i)