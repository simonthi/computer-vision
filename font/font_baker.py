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
    char = f.readline().strip('\n')
print(char)
print(len(char))    

font = fontforge.open('font/Computer-Vision.sfd')

if(len(char) == 0):
    sys.exit()

if(len(char) > 1):
    if(font.findEncodingSlot(char) != -1):
        print("Alert")
        counter = 1
        while(font.findEncodingSlot(char+".alt"+str(counter)) != -1):
            counter = counter + 1
        glyph = font.createChar(-1, char+".alt"+str(counter))
    else:
        glyph = font.createChar(-1, char)
        fea = fea_writer("liga-1", glyph, char)
    glyph.importOutlines('mpost/output-svg/65.svg')
    glyph.right_side_bearing = int(glyph.left_side_bearing)
    

else:
    char_uni = int(get_uni(char), 16)
    print(char_uni)
    if(font.findEncodingSlot(char_uni) != -1):
        print("Alert")
        counter = 1
        while(font.findEncodingSlot(char+".alt"+str(counter)) != -1):
            counter = counter + 1
        glyph = font.createChar(-1, char+".alt"+str(counter))
    else:
        glyph = font.createChar(char_uni)
    glyph.importOutlines('mpost/output-svg/65.svg')
    glyph.right_side_bearing = int(glyph.left_side_bearing)
    

font.save('font/Computer-Vision.sfd')