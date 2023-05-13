from collections.abc import Iterable

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    
    if not isinstance(iterable, Iterable):
        raise TypeError("iterable must be a list or tuple ...")
    if len(iterable) < 1:
        raise ValueError("iterable must not be empty")
    itett = iterable.copy()
    itett.clear()
    for elm in iterable:
        if function_to_apply(elm):
            itett.append(elm)
    return itett
x = [1, 2, 3, 4, 5]

# ft_filter(lambda dum: not (dum % 2), x)
l = list(ft_filter(lambda dum: not (dum % 2), x))
print(l)