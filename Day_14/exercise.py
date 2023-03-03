def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print('Add Five',add_five)
result = add_five(6)
print(result)

def add(x,y):
    return x + y
def calculate(func,x,y):
    return func(x,y)

result = calculate(add,4,6)
print(result)

def greeting(name):
    def hello():
        return 'Hello' + name + '!'
    return hello
greet = greeting('Alious')
print(greet())
