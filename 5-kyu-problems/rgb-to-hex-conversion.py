"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:
"""

def rgb(r, g, b):
    # Clamp values to range 0-255
    r = min(max(r, 0), 255)
    g = min(max(g, 0), 255)
    b = min(max(b, 0), 255)
    
    # Convert RGB to Hex values
    hex_r = hex(r)[2:].rjust(2, "0").upper()
    hex_g = hex(g)[2:].rjust(2, "0").upper()
    hex_b = hex(b)[2:].rjust(2, "0").upper()
    
    return hex_r + hex_g + hex_b