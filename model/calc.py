
def get_plates(weight, bar=45, sizes=[45,25,10,5,2.5]):
    """Calculates plates to be added to each end of bar."""
    weights = dict()
    if weight - bar < 0:
        raise LessThanBar
    remaining = weight - bar
    smallest = min(sizes)
    if remaining % (smallest*2) > 0:
        raise NotDivisible
    sizes.sort(reverse=True)
    for s in sizes:
        num = int(remaining // (s*2))
        remaining = remaining % (s*2)
        if num > 0:
            weights.update({s:num})
    return weights

def get_list(string):
    the_list = [float(s) for s in string.split(',')]
    for i in the_list:
        if i % 1 == 0:
            i = int(i)
    return the_list

class LessThanBar(ValueError):
    """Raised when weight is less than bar."""
    pass

class NotDivisible(ValueError):
    """Raised when weight not divisible by smallest plate."""
    pass

