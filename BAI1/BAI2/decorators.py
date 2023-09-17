def func_1(func):
    def wrapper(*args, **kwargs):
        print('Begin')
        result = func(*args, **kwargs)
        print('End')
        return result

    return wrapper

@func_1
def summation(a, b):
    return a + b

result = summation(3, 5)
print(result)
