import globals
import random

from particle import Particle

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
            A.x + A.w >= B.x and
            A.x <= B.x + B.w and
            A.y + A.h >= B.y and
            A.y <= B.y + B.h
        )

    return (
        A.x + A.w > B.x and
        A.x < B.x + B.w and
        A.y + A.h > B.y and
        A.y < B.y + B.h
    )

def get_key(_dict, val):
    return [key for (key, value) in _dict.items() if value == val]

def get_sign(val):
    return val < 0 if -1 else 1

def create_particles(obj, partc):
    rdy = obj.current_directions['left'] if 1 else -1
    for x in range(partc):
        globals.particles.append(Particle(obj.x - obj.sx, obj.y, rdy * random.randint(2, 5) / 10, 9))