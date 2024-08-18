# Computer/Vision

![A photo of a television screen. The screen is split into three: Metafont code on the left, the generated sign in the middle, and the recognized text on the right. Below, the latest additions to the font are displayed on light blue background.](https://github.com/user-attachments/assets/c15af74c-5567-4384-9464-e55759c29b25)


## What is this?
_Computer/Vision_ is an artwork conceived by Simon Thiefes and originally made for the exhibiton [Quasi experimental writing systems](https://hmctartcenter.org/exhibitions/quasi-experimental-writing-systems/) at the Hoffmitz Milken Center for typography at ArtCenter, Pasadena.  

Artist statement:

*It is quite easy to have a concept of a given letter i.e., an A or an Ω. It is not too difficult to tell As from non-As such as B or any other letter. Yet, to come up with a set of rules to describe what makes an A an A, is a more complicated endeavor. But what if you have to decide? What if you are given a randomly created letter and you need to say what it is?
Computer/Vision is an invitation to think about the limits of computation. What does it mean to have clear cut categories? Without the possibility of blurry borders, of nuance?
This work explores these questions by giving a computer full control over the random creation of letters, their labelling using text recognition, and their inclusion into a writing system. 
Computer/Vision will evolve during the exhibition period, adding more and more characters to a font, that is open source and available for download.*

## The exhibtion

![An exhibition view of Computer Vision at the HMCT Art Center](https://github.com/user-attachments/assets/5ea816ac-6f00-495a-83fa-2314bfacbd15)

Throughout the exhibition period (November 17, 2023 – April 28, 2024), one Raspberry Pi 4 ran the Python script, that generated the signs and displayed everything on screen, non stop. During that time, not one but twenty five fonts came into being. The working files got regularly pushed to this repository.

https://github.com/user-attachments/assets/a2af4c44-7a90-4aac-ad2e-278fc080ce8c

> A screen capture of Computer Vision. The screen is split into three: the Metafont code on the left, the generated sign in the middle, and the recognized text on the right. Below, the latest additions to the font are displayed.


## Getting and using the fonts

The fonts are now available from [this repository](/output) for download. They are licensed under the OFL license. 

I decided against postprocessing the fonts, as this would speak against the concept of the artwork. This means, that not all fonts are usable — usable in that sense that you could probably not utilize them as is in your designs: most of them do neither have a space character nor all the letters of the alphabet. This is a feature not a bug! 

As allowed per the license terms you are more than welcome to explore and modify the fonts for your use cases. I would be happy if you share your uses!

---

## Running Computer/Vision at home // Installation instructions

Thank you for your interest in running _Computer/Vison_ at home. The installation relies on a few Open Source projects. Thank you to all the contributors of these projects.

Back to business:
Make sure you are running on Unix like system or macOS. 
Install a recent version of Python, preferebly directly from python.org.
Once that is done, install the requirements:

`python3 -m install requirements.txt`

Further packages you will need:

* Git
* Make sure you have PIL and ImageTK installed:
`sudo apt-get install python3-pil python3-pil.imagetk`

* Get a TeX package including Metapost i.e. Texlive
`sudo apt install texlive`
`sudo apt-get install texlive-metapost`
* Get Tesseract
`sudo apt install tesseract-ocr`
* And get Fontforge
`sudo apt-get -y install python3-fontforge`

Bravo, you are nearly there. You just need to cd into your directory that you cloned this repo to and run the script:
`python3 main.py`

Voilà you have a home exhibition of _Computer/Vision_.
