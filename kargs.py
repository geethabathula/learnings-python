def favorite_colors(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")

favorite_colors(rusty='green', colt='blue')

def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message','The result is')} {int(operation_value)}"
    return final

h = calculate(make_float=True, operation='divide', first=3.5, second=5)
print(h)

# rusty's favorite color is green
# colt's favorite color is blue