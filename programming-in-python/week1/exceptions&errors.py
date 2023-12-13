# Errors 

def divide_by(a, b):
    return a/b

try:
    ans = divide_by(30,0)
except ZeroDivisionError as e:
    print(e, "We cannot divide by zero")
except Exception as e:
    print(e, "something went wrong")