import pyxel

import util.helper

def render_bounds(entities, col):
    for entity in entities:
        pyxel.rectb(entity.x, entity.y, entity.w, entity.h, col)

def render_collision_areas(entities, col):
    for entity in entities:
        if entity.dynamic_entity:
            pyxel.rectb(
                entity.collision_check_area.x, 
                entity.collision_check_area.y, 
                entity.collision_check_area.w, 
                entity.collision_check_area.h, 
                col
            )

def tile_data(width, height, tilesize, tilemap, offsetx, offsety):
    grid_color = 8
    cursor_color = 7
    bg_color = 0

    mx = util.helper.clamp(pyxel.mouse_x - 2, 0, width)
    my = util.helper.clamp(pyxel.mouse_y - 2, 0, height)

    cols = width // tilesize
    rows = height // tilesize

    for col in range(cols):
        pyxel.line(col * tilesize, 0, col * tilesize, height, grid_color)

    for row in range(rows):
        pyxel.line(0, row * tilesize, width, row * tilesize, tilesize)

    if mx > width / 2:
        text_offsetx = -12
    else:
        text_offsetx = 12

    if my > height / 2:
        text_offsety = -12
    else:
        text_offsety = 12

    pyxel.rectb(mx - (mx % tilesize), my - (my % tilesize), tilesize, tilesize, cursor_color)

    data = pyxel.tilemap(tilemap).get(offsetx + mx // tilesize, offsety + my // tilesize)

    outputx = mx + text_offsetx
    outputy = my + text_offsety

    pyxel.rect(outputx, outputy, 16, 8, bg_color)
    pyxel.text(outputx + 2, outputy + 2, str(data), cursor_color)