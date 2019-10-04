# Understanding Keyword Arguments
def print_kwargs(**kwargs):
    print(kwargs)


some_dictionary = {'key01': 'foo', 'key02': 'bar'}
print_kwargs(**some_dictionary)


# Kwargs V2
def print_kwargs_v2(lat=None, long=None):
    print(lat, long)


data = {'lat': 0.9, 'long': 1.9}
print_kwargs_v2(**data)


# Kwargs V3
def print_kwargs_v3(lat=None, long=None, **kwargs):
    print(lat, long, kwargs)


print_kwargs_v3(1, 5, data='Hello Kwargs')
