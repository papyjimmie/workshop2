x = "awesome"


def myFunc():
    global x
    print("Python is " + x)
    x = "fantastic"


myFunc()
print("Python is  " + x)