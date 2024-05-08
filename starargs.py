def sum_all_values(num1,num2,num3):
    return num1+num2+num3
print(sum_all_values(1,2,3))
#Instead using *args we can pass as many parameters as we want
#as it returns a tuple we are looping over the tuple using for
def sum_all_values(*args):
    total = 0
    for val in args:
        total += val

    return total

print(sum_all_values(1, 2, 3)) # 6

print(sum_all_values(1, 2, 3, 4, 5)) # 15

def ensure_correct_info(*args):
    if "Geetha" in args and "Supriya" in args:
        return "Welcome back Geetha!"

    return "Not sure who you are..."

print(ensure_correct_info()) # Not sure who you are...

print(ensure_correct_info(1, True, "Geetha", "Supriya")) #Welcome back Geetha!