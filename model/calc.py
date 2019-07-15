
def get_plates(weight, sizes=[45,25,10,5,2.5], bar=45):
    weights = dict()
    if weight - bar < 0:
        raise LessThanBar
    plate_weight = weight - bar
    smallest_plate = min(sizes)
    if plate_weight % smallest_plate > 0:
        raise NotDivisible
    return weights

class LessThanBar(ValueError):
    pass

class NotDivisible(ValueError):
    pass

