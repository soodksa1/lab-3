def repeat_hello(num_repetitions):
    def decorator_hello(func):
        def wrapper_hello():
            for _ in range(num_repetitions):
                func()
        return wrapper_hello
    return decorator_hello

x= int(input("Enter a number of repetitions"))
# Write your decorator here




@repeat_hello(x)
def hello():
    print ('Hello')

hello()
