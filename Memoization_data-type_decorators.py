"""
This project implements decorators that implement Memoization and data type checking of the input parameters of the function.

This project is based on a project "Python Decorators Practice, from zero to hero" from the datawars website.
"""
from functools import wraps # preserve the decorated function's name and docs

def double(func):
    """
    The decorator double the return value of any function that returns a numeric value.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return inner

@double
def add(x, y):
    return x + y


def check_numeric(func):
    """
    The decorator check that ALL the parameters passed are of numeric type.
    If any parameter is NOT numeric, the function raise a ValueError exception.
    """
    @wraps(func)
    def _check_numeric(*args, **kwargs):
        numeric_types = [isinstance(arg, (float, int, complex)) for arg in args]
        numeric_types = all(numeric_types)
        if numeric_types:
            return func(*args, **kwargs)
        else:
            raise ValueError 
    return _check_numeric


@check_numeric
def add2(*args):
    return sum(args)


def enforce_type(type_to_check):
    """
    The enforce_type decorator receives a parameter, the type to enforce in the function, 
    and raises a ValueError if the decorated function is invoked with arguments that are not of the indicated type.
    """
    def _enforce_type(func):
        @wraps(func)
        def __enforce_type(*args, **kwargs):
            numeric_types = [isinstance(arg, type_to_check) for arg in args]
            numeric_types = all(numeric_types)
            if numeric_types:
                return func(*args, **kwargs)
            else:
                raise ValueError 
        return __enforce_type
    return _enforce_type

@enforce_type(int)
def add3(x, y):
    return x + y


class enforce_type_class:
    """
    The enforce_type_class decorator works in the same way as the previous decorator, 
    but this time re-implemented as a class.
    """
    def __init__(self, type_to_check):
        self.type_to_check = type_to_check

    def __call__(self, func):
        @wraps(func)
        def _enforce_type(*args, **kwargs):
            numeric_types = [isinstance(arg, self.type_to_check) for arg in args]
            numeric_types = all(numeric_types)
            if numeric_types:
                return func(*args, **kwargs)
            else:
                raise ValueError
        return _enforce_type
    
@enforce_type_class(int)
def add4(x, y):
    return x + y


def memoize(func):
    @wraps(func)
    def _memoize(*args, **kwargs):
        result = func(*args, **kwargs)
        
        _memoize.previous_calls.append({
            "arguments": args,
            "result": result
        })
        return result
    _memoize.previous_calls = []
    return _memoize

@memoize
def add5(x, y):
    return x + y


if __name__=="__main__":
    print("Example for '@double':", add(2, 3)) #10
    print("Example for '@check_numeric':", add2(7, 2.1, 1, 3+1j)) #(13.1+1j)
    print("Example for '@enforce_type':", add3(2, 3)) #5
    print("Example for '@enforce_type_class':", add4(3, 3)) #6
    add5(2, 3)
    add5(1, 1)
    print("Example for '@memoize', add5.previous_calls:", add5.previous_calls) 
    #[{'arguments': (2, 3), 'result': 5}, {'arguments': (1, 1), 'result': 2}]