transform common(x = 0):
    subpixel True
    transform_anchor True
    xcenter 0.5
    yanchor 1.0
    ypos 1080
    on show:
        # This block is called when the image is first shown.
        alpha 0
        xoffset x
        linear 0.25 alpha 1
    on replaced:
        alpha 1
        linear 0.25 alpha 0
        ease 0.75 xoffset x

# This is so that characters don't blip out of existence.
# Use "show x at transform_hide", then "hide x" to hide a given character
transform transform_hide:
    on hide:
        linear 0.45 alpha 0


#Standard positioning for characters
transform centered:
    common()

transform center_right:
    common(300)

transform center_left:
    common(-300)

transform embiggen:
    size (600, 1080)
    ease 1 size (600 * 1.1, 1080 * 1.1)