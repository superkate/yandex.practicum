class TooLongDistanceForFragilePackageException(Exception):
    "Raised when is_fragile == True and distance > 30"
    pass

class DistanceIsLessThanOrEqualToZeroException(Exception):
    "Raised when distance <= 0"
    pass

def calculate_delivery_cost(distance, is_big, is_fragile, delivery_load = ""):
    min_delivery_cost = 400
    delivery_cost = 0

    if distance <= 0:
        raise DistanceIsLessThanOrEqualToZeroException

    if is_fragile:
        if distance <= 30:
            delivery_cost += 300
        else:
            raise TooLongDistanceForFragilePackageException

    if distance <= 2:
        delivery_cost += 50
    elif distance <= 10:
        delivery_cost += 100
    elif distance <= 30:
        delivery_cost += 200
    else:
        delivery_cost += 300

    if is_big:
        delivery_cost += 200
    else:
        delivery_cost += 100

    match delivery_load:
        case "very high":
            delivery_cost *= 1.6
        case "high":
            delivery_cost *= 1.4
        case "increased":
            delivery_cost *= 1.2
        case _:
            delivery_cost *= 1

    return delivery_cost if delivery_cost >= min_delivery_cost else min_delivery_cost
