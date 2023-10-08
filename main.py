#import fontforge
import os

from subprocess import call

import random

import sched, time

from PIL import Image, ImageTk

import pytesseract

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

import tkinter as tk

import cairosvg

import time
    
    
COLORS = ['blue', 'yellow', 'orangered', 'darkorange', 'darkviolet', 'springgreen']    
l = ['mpost/output-svg/1.png', 'mpost/output-svg/2.png', 'mpost/output-svg/3.png', 'mpost/output-svg/4.png', 'mpost/output-svg/5.png']
disp_l=['mpost/output-svg/1.png', 'mpost/output-svg/2.png', 'mpost/output-svg/3.png', 'mpost/output-svg/4.png', 'mpost/output-svg/5.png']
latest = ['mpost/output-svg/1.png', 'mpost/output-svg/2.png', 'mpost/output-svg/3.png', 'mpost/output-svg/4.png', 'mpost/output-svg/5.png']

t = time.localtime()
curr = time.strftime("%m-%d-%Y, %H:%M:%S", t)

global glyph_counter
glyph_counter = 0
    
root = tk.Tk()
root.wm_title('Computer/Vision')
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.attributes('-fullscreen', True)
canvas = tk.Canvas(root,  highlightthickness=0)
img_path = 'mpost/output-svg/65.png'
image = Image.open(img_path)
img_width, img_height = image.size 
img = ImageTk.PhotoImage(image, size=(img_width, img_height))
char_img = canvas.create_image(width/2-img_width/2, height/2-img_height/2-100, image=img, tag="main_img", anchor="nw")
canvas.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
with open("font/temp.txt", 'r') as f:
    char = f.readline().strip('\n')
text = canvas.create_text(2*width/3+width/3/2, height/2-200, text = char, font = ("monono", 128), anchor="n")  
code = canvas.create_text(64, height/2-100, text = "", font = ("monono", 12), anchor="w")  
descr1 = canvas.create_text(width/3/2, 24, text = "Random Character Description\ngenerated @"+str(curr)+" CEST", font = ("monono", 12), anchor="n")
canvas.create_line(width/3, 0, width/3, height-200, fill="black", tags="line")
descr2 = canvas.create_text(width/2, 24, text = "Generated Sign", font = ("monono", 12), anchor="n")
canvas.create_line(2*width/3, 0, 2*width/3, height-200, fill="black", tags="line")
descr3 = canvas.create_text(2*width/3+width/3/2, 24, text = "Recognized Text", font = ("monono", 12), anchor="n")
canvas.create_line(0, height-200, width, height-200, fill="black", tags="line")
descr4 = canvas.create_text(24, height-160, text = "Latest Additions to font", font = ("monono", 12), anchor="sw")
for i in range(5):
    l[i] = Image.open("mpost/output-svg/"+str(i)+".png")
    l[i] = ImageTk.PhotoImage(l[i])
    disp_l[i] = l[i]._PhotoImage__photo.subsample(5, 5)
    latest[i] = canvas.create_image(36+160*i, height-24, image=disp_l[i], anchor="sw")
root.update()  



        
def main_loop(scheduler): 
    scheduler.enter(10, 1, main_loop, (scheduler,))
    x = char_creator()
    print(x)
    with open('mpost/temp.mp', 'w') as t:
        t.write(x)
    os.system("mpost mpost/temp.mp")
    #drawing = svg2rlg("mpost/output-svg/65.svg")
    cairosvg.svg2png(url="mpost/output-svg/65.svg", write_to="mpost/output-svg/65.png")
    cairosvg.svg2png(url="mpost/output-svg/65.svg", write_to="mpost/output-svg/"+str(glyph_counter%5)+".png")
    custom_oem_psm_config = r'--oem 1 --psm 10'
    #renderPM.drawToFile(drawing, "mpost/output-svg/65.png", fmt="PNG")
    char = pytesseract.image_to_string(Image.open('mpost/output-svg/65.png'), config=custom_oem_psm_config)
    
    with open('font/temp.txt', 'w') as t:
        t.write(char)
    os.system('./cleaner.sh')
    print("cleaned")
    os.system("fontforge -script font/font_baker.py")
    
    display()
    root.update()  


def char_creator():
    global glyph_counter 
    glyph_counter = glyph_counter + 1
    char_width = random.randint(2, 10)

    num_coord = str(random.randint(3, 5))

    num_strokes = random.randint(2, 4)

    mp_code = "input mpost/def;\n"

    mp_code += "beginchar(65,"+str(char_width)+");\n" 

    for a in range(1, int(num_strokes)):
        num_strokes = random.randint(1, 4)
        num_coord = str(random.randint(3, 5))
        for h in range(1, int(num_coord)):
            mp_code += "\tx"+str(a*h*num_strokes)+" := "+str(random.randint(0, char_width))+" * ux;\n"
            mp_code += "\ty"+str(a*h*num_strokes)+" := "+str(random.randint(-4, 8))+" * uy;\n"

        if (random.randint(0,1) == 0):
            if (random.randint(0,1) == 0):
                mp_code +="pickup pencircle xscaled (strokeX/"+str(random.randint(1,10))+") yscaled (strokeY/"+str(random.randint(1,10))+");\n"
            else:
                mp_code +="pickup pencircle xscaled (strokeX/"+str(random.randint(1,10))+") yscaled (strokeY/"+str(random.randint(1,10))+");\n"
        mp_code += "draw "
        for i in range(1, (int(num_coord)-1)):
            mp_code += "z"+str(a*i*num_strokes)
            if (random.randint(0,1) == 0):
                mp_code += "--"
            else:
                mp_code += ".."

        mp_code += "z"+str((int(num_coord)-1)*num_strokes*a)+";\n"

    mp_code += "endchar("+str(int(num_coord)-1)+");\nend."
    return(mp_code)



def display():
    canvas.configure(bg=random.sample(COLORS, 1)[0])
    canvas.itemconfigure(text, text="")
    canvas.itemconfigure(code, text="")
    canvas.itemconfigure(char_img, image=None)
    canvas.image=None
    root.update() 
    time.sleep(1)
    with open('mpost/temp.mp', 'r') as t:
        x = t.read()
    canvas.itemconfigure(code, text=x)
    t = time.localtime()
    curr = time.strftime("%m-%d-%Y, %H:%M:%S", t)
    canvas.itemconfigure(descr1, text="Random Character Description\ngenerated @"+str(curr)+" CEST")
    root.update()  
    time.sleep(3)
    img_path = 'mpost/output-svg/65.png'
    image = Image.open(img_path)
    img_width, img_height = image.size 
    img2 = ImageTk.PhotoImage(image, size=(img_width, img_height))
    canvas.itemconfigure(char_img, image=img2)
    canvas.coords(char_img, width/2-img_width/2, 0)
    for i in range(5):
        l[i] = Image.open("mpost/output-svg/"+str((-i+glyph_counter)%5)+".png")
        l[i] = ImageTk.PhotoImage(l[i])
        disp_l[i] = l[i]._PhotoImage__photo.subsample(5, 5)
        canvas.itemconfigure(latest[i], image=disp_l[i])
        canvas.image=l[i]
    canvas.image=img2
    root.update()  
    with open("font/temp.txt", 'r') as f:
        char = f.readline().strip('\n')
    time.sleep(3)
    canvas.itemconfigure(text, text=char)
    root.update()
    
    
def push():
    global glyph_counter
    scheduler.enter(120, 1, push)
    with open('font/no_glyphs.txt', 'r') as t:
        x = t.read()
    new_no_glyphs = int(x) + glyph_counter
    if (new_no_glyphs > 60000):
        with open('font/no_glyphs.txt', 'w') as t:
            t.write(str(0))
        glyph_counter = 0
        t = time.localtime()
        now = time.strftime("%y%m%d", t)
        os.system('mv font/Computer-Vision.sfd font/'+now+'Computer-Vision.sfd')
        os.system('cp font/blank.sfd font/Computer-Vision.sfd')
    else:
        with open('font/no_glyphs.txt', 'w') as t:
            t.write(str(new_no_glyphs))
    commit_message = "Adding current stage of font"
    os.system('git add font/\*.sfd')
    os.system('git commit -m "'+ commit_message +'"')
    os.system('git push origin computer-1@exhibition')
    
    

scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(0, 1, main_loop, (scheduler,))
scheduler.enter(1, 1, push)
scheduler.run()