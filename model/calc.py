
def get_plates(weight, sizes=[45,25,10,5,2.5], bar=45):
    weights = dict()
    if weight - bar < 0:
        raise LessThanBar
    return weights

class LessThanBar(ValueError):
    pass

