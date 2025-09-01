def outer():
    x = 1
    def inner():
        #use nonlocal x can change the value of x in the outer
        nonlocal x
        x += 1
        return x
    return inner

function = outer()
print(function())  # 2
print(function())  # 3