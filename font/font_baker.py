import fontforge
import os



with open("font/temp.txt", 'r') as f:
    char = f.read()
print(char)

font = fontforge.open('font/blank.sfd')

glyph = font.createChar(-1, char)
glyph.importOutlines('mpost/output-svg/66.svg').simplify()
glyph.right_side_bearing = int(glyph.left_side_bearing)


font.generate('font/testfont.otf')