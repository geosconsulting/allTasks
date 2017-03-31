def function(a, b):
    print("A function")

    #funzione locale
    def local_function(x, y):
        print("A local function")
        return x*y+a+b

    return local_function

p = function(5, 7)



