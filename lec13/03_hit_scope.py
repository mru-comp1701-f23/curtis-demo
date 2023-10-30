def is_hit(d1: float, d2: float) -> bool:
    """
    Checks if d1 and d2 are within 10 m
    """
    # hit = False
    if d1 > d2:
        hit = d1 - d2 < 10
    else:
        hit = d2 - d1 < 10
    return hit

def is_hit_awkward(d1: float, d2: float) -> bool:
    """
    Checks if d1 and d2 are within 10 m
    """
    hit = False
    if d1 > d2:
        if d1 - d2 < 10:
            hit = True
    else:
        if d2 - d1 < 10:
            hit = True
    return hit

def main() -> None:
    is_hit(10, 15)
    is_hit(10, 30)
    is_hit_awkward(10, 15)
    is_hit_awkward(10, 30)

main()