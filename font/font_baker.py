import fontforge
import os
import re


def get_uni(string):
    res = (re.sub('.', lambda x: r'%04X' % ord(x.group()), string))
    return res



def fea_writer(table, glyph, chars):
    sub = ""
    for i in range(len(chars)):
        sub = sub+ " " + chars[i]
    print(sub)    
    glyph.addPosSub(table, sub)

    
    
with open("font/temp.txt", 'r') as f:
    char = f.read()
print(char)
char_uni = int(get_uni(char), 16)
print(char_uni)

font = fontforge.open('font/blank.sfd')

if(len(char) > 1):
    if(font.createChar(-1, char) != -1):
        print("Alert")
        counter = 1
        while(font.findEncodingSlot(char+".alt"+str(counter)) != -1):
            counter = counter + 1
        glyph = font.createChar(-1, char+".alt"+str(counter))
    else:
        glyph = font.createChar(-1, char)
    glyph.importOutlines('mpost/output-svg/65.svg')
    glyph.right_side_bearing = int(glyph.left_side_bearing)
    fea = fea_writer("liga-1", glyph, char)

else:
    if(font.createChar(-1, char_uni) != -1):
        print("Alert")
        counter = 1
        while(font.findEncodingSlot(char_uni+".alt"+str(counter)) != -1):
            counter = counter + 1
        glyph = font.createChar(-1, char_uni+".alt"+str(counter))
    else:
        glyph = font.createChar(-1, char_uni)
    glyph.importOutlines('mpost/output-svg/65.svg')
    glyph.right_side_bearing = int(glyph.left_side_bearing)
    

font.save('font/blank.sfd')
font.generate('font/testfont.otf')


