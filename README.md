# Computer/Vision

## What is this?
_Computer/Vision_ is an artwork conceived by Simon Thiefes and originally made for the exhibiton [Quasi experimental writing systems](https://hmctartcenter.org/exhibitions/quasi-experimental-writing-systems/) at the Hoffmitz Milken Center for typography at ArtCenter, Pasadena.  

It runs on low key computing equipment. If you want to run it at home see installation instructions below.

Artist statement:
It is quite easy to have a concept of a given letter i.e., an A or an Ω. It is not too difficult to tell As from non-As such as B or any other letter. Yet, to come up with a set of rules to describe what makes an A an A, is a more complicated endeavor. But what if you have to decide? What if you are given a randomly created letter and you need to say what it is?
Computer/Vision is an invitation to think about the limits of computation. What does it mean to have clear cut categories? Without the possibility of blurry borders, of nuance?
This work explores these questions by giving a computer full control over the random creation of letters, their labelling using text recognition, and their inclusion into a writing system. 
Computer/Vision will evolve during the exhibition period, adding more and more characters to a font, that is open source and available for download.

## Getting and using the fonts

The fonts will be regularly published at this place and tracked in the Releases section. The fonts are published under OFL license.

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

Voilà you have a home exhibition of _Computer/Vision_
