from functools import wraps
def count_check(function, count=[0]):
    """Returns number of times any function with this decorator is called
    """
    @wraps(function)
    def increase_count(*args, **kwargs):
        count[0] += 1
        return function(*args, **kwargs), count[0]

    return increase_count

@count_check
def foo():
    return 42

print(foo(), foo(), foo(), foo())


@count_check
def bar():
    return 23

print(bar(), bar(), bar())