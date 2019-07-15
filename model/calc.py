
def get_plates(weight, sizes=[45,25,10,5,2.5], bar=45):
    weights = dict()
    if weight - bar < 0:
        raise LessThanBar
    remaining = weight - bar
    smallest = min(sizes)
    if remaining % smallest > 0:
        raise NotDivisible
    return weights

class LessThanBar(ValueError):
    pass

class NotDivisible(ValueError):
    pass

