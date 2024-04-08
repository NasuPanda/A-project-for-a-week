def repeater(old_func):
    def new_fun(*args, **kargs):
        # Call the old func
        old_func(*args, **kargs)
        # Call it twice
        old_func(*args, **kargs)

    return new_fun

@repeater
def multiply(num1, num2):
    print(num1, num2)

multiply(2,3)
