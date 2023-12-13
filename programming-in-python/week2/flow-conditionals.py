# a = True
# b = True

# if a and b:
#     print("all true!")

http_status = 404

match http_status:
    case 200 | 201:
        print("success")
    case 400:
        print("client error")
    case 404:
        print("not found")
    case 500:
        print("server error")
    case _:
        print("unknown")
        