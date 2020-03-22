def clamp(val, val_min, val_max):
    if val < val_min:
        val = val_min
    elif val > val_max:
        val = val_max

    return val