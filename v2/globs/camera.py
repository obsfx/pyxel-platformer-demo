import random

x = 0
y = 0
duration = 0
offset = 0
base = 0

def shake():
    global x
    global y

    x = base + random.randint(-offset, offset)
    y = base + random.randint(-offset, offset)

def init_shake(_duration, _offset, _base):
    global duration
    global offset
    global base

    duration = _duration
    offset = _offset
    base = _base