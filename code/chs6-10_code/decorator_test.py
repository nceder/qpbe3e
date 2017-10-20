def decorate(func):
    print("in decorate function, decorating", func.__name__)  #A
    def wrapper_func(*args):
        print("Executing", func.__name__)
        return func(*args)
    return wrapper_func                                       #B

@decorate                                             #C
def myfunction(parameter):
    print(parameter)

if __name__ == "__main__":
    myfunction("hello")
