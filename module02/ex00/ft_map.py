from collections.abc import Iterable
def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
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
    iterr = iterable.copy()
    iterr.clear()
    for elm in iterable:
        elm = function_to_apply(elm)
        iterr.append(elm)
    return iterr
x = [1]
e = list(ft_map(lambda t: t + 1, x))
print(e)
