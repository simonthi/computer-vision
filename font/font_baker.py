import fontforge
import os


with open("font/temp.txt", 'r') as f:
    char = f.read()
print(char)


font = fontforge.open('font/blank.sfd')

glyph = font.createChar(-1, char)
glyph.importOutlines('mpost/output-svg/65.svg')
glyph.right_side_bearing = int(glyph.left_side_bearing)

font.save('font/blank.sfd')
font.generate('font/testfont.otf')



