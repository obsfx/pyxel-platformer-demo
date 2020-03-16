import globals
import random
import time

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

def create_particles(obj, partc, col, blood=False):
    rdy = -1

    px = obj.x

    rm = 2
    rx = 4

    if obj.current_directions['left']:
        rdy = 1
        px += 4

    if blood:
        rdy *= -1
        px = obj.x
        rm = 1
        rx = 30
    random.seed(time.time())

    for x in range(partc):
        globals.particles.append(Particle(px, obj.y, rdy * random.randint(rm, rx) / 10, col, True))