############## Read File ##################

# file = open("test.txt", mode = "r")

# data = file.readline()

# print(data)

# file.close()

# with open("test.txt", mode="r") as file:
#     data = file.readline()

#     print(data)

############# Create files #################

# override
# with open("new_file.txt", mode="w") as file:
#     file.writelines(["This is a new file created!", "\nNew line added yeee"])

# append
# try:
#     with open("sample/new_file.txt", mode="a") as file:
#         file.writelines(["\nThis is a new file created!", "\nNew line added yeee"])
# except FileNotFoundError as e:
#     print("Error: ", e)

########### Read Lines #######################

with open("sample.txt", mode="r") as file:
    #print(file.read()) # reads all the file
    print(file.read(44)) # reads n number of characters