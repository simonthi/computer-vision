#import fontforge
import os

import random

import sched, time

from PIL import Image, ImageTk

import pytesseract

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

import tkinter as tk

import cairosvg
    
    
    
COLORS = ['blue', 'yellow', 'orangered', 'darkorange', 'darkviolet', 'springgreen']    
    
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
char_img = canvas.create_image(width/2-img_width/2, 0, image=img, tag="main_img", anchor="nw")
canvas.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
with open("font/temp.txt", 'r') as f:
    char = f.readline().strip('\n')
text = canvas.create_text(width/2, height-128, text = char, font = ("monono", 32))    
root.update()  



        
def main_loop(scheduler): 
    # schedule the next call first
    scheduler.enter(30, 1, main_loop, (scheduler,))
    x = char_creator()
    print(x)
    with open('mpost/temp.mp', 'w') as t:
        t.write(x)
    os.system("mpost mpost/temp.mp")
    #drawing = svg2rlg("mpost/output-svg/65.svg")
    cairosvg.svg2png(url="mpost/output-svg/65.svg", write_to="mpost/output-svg/65.png")
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
    img_path = 'mpost/output-svg/65.png'
    image = Image.open(img_path)
    img_width, img_height = image.size 
    img2 = ImageTk.PhotoImage(image, size=(img_width, img_height))
    canvas.itemconfigure(char_img, image=img2)
    canvas.coords(char_img, width/2-img_width/2, 0)
    canvas.image=img2
    with open("font/temp.txt", 'r') as f:
        char = f.readline().strip('\n')
    canvas.itemconfigure(text, text=char)
    
    


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(0, 1, main_loop, (scheduler,))
scheduler.run()