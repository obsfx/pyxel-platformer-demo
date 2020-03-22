class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_left(self):
        return self.x

    def get_right(self):
        return self.x + self.w

    def get_top(self):
        return self.y
    
    def get_bottom(self):
        return self.y + self.h

    def get_mid_x(self):
        return self.x + self.get_half_width()

    def get_mid_y(self):
        return self.y + self.get_half_height()

    def get_half_width(self):
        return self.w * 0.5

    def get_half_height(self):
        return self.h * 0.5