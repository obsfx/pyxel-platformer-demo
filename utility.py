def AABB_collision(objA, objB, include_borders=False):
    A = objA
    B = objB

    objA_area = objA.w * objA.h
    objB_area = objB.w * objB.h

    if objA_area > objB_area:
        A = objB
        B = objA

    if include_borders:
        return (
            A.x + A.w >= B.x - B.w and
            A.x - A.w <= B.x + B.w and
            A.y + A.h >= B.y - B.h and
            A.y - A.h <= B.y + B.h
        )

    return (
        A.x + A.w > B.x - B.w and
        A.x - A.w < B.x + B.w and
        A.y + A.h > B.y - B.h and
        A.y - A.h < B.y + B.h
    )