from collections.abc import Iterable
import functools
def return_value(iterable):
    for elm in iterable:
        yield elm

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not isinstance(iterable, Iterable):
        raise TypeError("iterable must be a list or tuple ...")
    if len(iterable) < 1:
        raise ValueError("iterable must not be empty")
    gett = return_value(iterable)
    lst = next(gett)
    for elm in gett:
        lst = function_to_apply(lst, elm)
    return lst


lst = ['h', 'o', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
lst = [2,3,5]
lst = {"name":lst, "value":20}
lst2 = ft_reduce(lambda u, v: u + v, lst)
print(lst2)
