def check(A, B, include_borders=False):
    l1 = A.get_left()
    r1 = A.get_right()
    t1 = A.get_top()
    b1 = A.get_bottom()

    l2 = B.get_left()
    r2 = B.get_right()
    t2 = B.get_top()
    b2 = B.get_bottom()

    midx1 = A.get_mid_x()
    midy1 = A.get_mid_y()

    midx2 = B.get_mid_x()
    midy2 = B.get_mid_y()

    if include_borders:
        condition = r1 <= l2 or l1 >= r2 or b1 <= t2 or t1 >= b2
    else:
        condition = r1 < l2 or l1 > r2 or b1 < t2 or t1 > b2

    if condition:
        return False
    else:
        return True

def resolve(A, B):
    new_pos = [ A.x, A.y ]

    deltas = get_deltas(A, B)

    dx = deltas['dx']
    dy = deltas['dy']
    abs_dx = deltas['abs_dx']
    abs_dy = deltas['abs_dy']
    abs_dxy = deltas['abs_dxy']

    A.x = B.x - A.w
    A.y = B.y - A.h

    ref_deltas = get_deltas(A, B)

    ref_abs_dx = ref_deltas['abs_dx']
    ref_abs_dy = ref_deltas['abs_dy']
    ref_abs_dxy = ref_deltas['abs_dxy']

    normalized_abs_dx = abs(abs_dx - ref_abs_dx)
    normalized_abs_dy = abs(abs_dy - ref_abs_dy)
    normalized_abs_dxy = abs(abs_dxy - ref_abs_dxy)

    if normalized_abs_dxy < 0.1:
        if dx < 0:
            new_pos[0] = B.x - A.w
        else:
            new_pos[0] = B.x + B.w

        if dy < 0:
            new_pos[1] = B.y - A.h
        else:
            new_pos[1] = B.y + B.h
    elif normalized_abs_dx < normalized_abs_dy:
        if dx < 0:
            new_pos[0] = B.x - A.w
        else:
            new_pos[0] = B.x + B.w
    else:
        if dy < 0:
            new_pos[1] = B.y - A.h
        else:
            new_pos[1] = B.y + B.h


    return new_pos

def get_deltas(A, B):
    midx1 = A.get_mid_x()
    midy1 = A.get_mid_y()

    midx2 = B.get_mid_x()
    midy2 = B.get_mid_y()

    dx = (midx1 - midx2) / A.get_half_width()
    dy = (midy1 - midy2) / A.get_half_height()

    abs_dx = abs(dx)
    abs_dy = abs(dy)

    return {
        'dx': dx,
        'dy': dy,
        'abs_dx': abs_dx,
        'abs_dy': abs_dy,
        'abs_dxy': abs(abs_dx - abs_dy)
    }