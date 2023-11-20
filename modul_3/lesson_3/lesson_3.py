
def multiple(nums):
    def inner(function):
        def wrapper(*args, **kwargs):
            re = function(*args, **kwargs)
            return re * nums
        return wrapper
    return inner

def division(nums):
    def inner(function):
        def wrapper(*args, **kwargs):
            re = function(*args, **kwargs)
            return re / nums
        return wrapper
    return inner


@division(3)
def add(*args):
    return sum(args)

print(add(1, 2, 3))