import fontforge
import os

font = fontforge.open('font/blank.sfd')

with open("font/temp.txt", 'r') as f:
    char = f.read()

directory = "mpost/output-svg"

print(char)

glyph = font.createChar(-1, char)
glyph.importOutlines(''+ directory + "/65.svg")
glyph.right_side_bearing = int(glyph.left_side_bearing)


font.generate('font/testfont.ttf')