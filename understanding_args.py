# Understanding Args and Kwargs
def print_args(d1, d2, d3):
    print(d1, d2, d3)


data = ('foo', 'bar', 'baz')
# print_args(data)  # It will return an ERROR because is passing the tuple only on the var "d1", d2 & d3 is missing
# use this to extract the data:
print_args(*data)


# ARGS V2
def print_args_v2(*args):
    for arg in args:
        print(arg)


print_args_v2(1, 2, 3, 4, 5)


# ARGS V3
def print_args_v3(*args):
    print(args)


# this will return the tuple
print_args_v3("Hello", 2, "Hi")


# ARGS Positional Arguments
def print_args_v4(a, b, c, *args):
    print(a, b, c, args)


print_args_v4(1, 2, 3, 4, 5, 6)


