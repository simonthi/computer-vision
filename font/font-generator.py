import fontforge
import os
   

font = fontforge.open('font/Computer-Vision.sfd')
font.generate('font/Computer-Vision.otf')