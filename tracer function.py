from functools import wraps


# decorator to trace execution of recursive function
def trace(func):

    # cache func name, which will be used for trace print
    func_name = func.__name__
    # define the separator, which will indicate current recursion level (repeated N times)
    separator = '|  '

    # current recursion depth
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs):

        # repeat separator N times (where N is recursion depth)
        # `map(str, args)` prepares the iterable with str representation of positional arguments
        # `", ".join(map(str, args))` will generate comma-separated list of positional arguments
        # `"x"*5` will print `"xxxxx"` - so we can use multiplication operator to repeat separator
        print(f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})')
        # we're diving in
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        # going out of that level of recursion
        trace.recursion_depth -= 1
        # result is printed on the next level
        print(f'{separator * (trace.recursion_depth + 1)}|-- return {result}')

        return result

    return traced_func


def mystery(a,b):
    if b==0:
        return 0
    if b%2==0:
        return mystery(a+a,b//2)
    return mystery(a+a,b//2)+a


# since the name of decorated func is the same as the name of original one
# decorator will be applied to nested calls too
mystery = trace(mystery)

# this will print all the recursion trace and the result at the bottom
print(mystery(10,50))
