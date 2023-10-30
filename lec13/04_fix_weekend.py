def is_awake(hour: float, day: str) -> bool:
    """Checks if a person is awake given time and day of week"""
    awake = False
    # if is_weekend(day) and (hour > 12 or hour < 2): # valid alternative
    if is_weekend(day): # assume this function exists
        if hour > 12 or hour < 2:
            awake = True
    elif hour > 8 and hour < 24: # indentation very important
        awake = True
    
    return awake