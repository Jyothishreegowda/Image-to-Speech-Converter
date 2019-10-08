#from PIL import Image
import PIL.Image
import pytesseract
from gtts import gTTS
import os
from tkinter import *
def cam():

    import cv2

    # Camera 0 is the integrated web cam on my netbook
    camera_port = 0

    #Number of frames to throw away while the camera adjusts to light levels
    ramp_frames = 30

    # Now we can initialize the camera capture object with the cv2.VideoCapture class.
    # All it needs is the index to a camera port.
    camera = cv2.VideoCapture(camera_port)

    # Captures a single image from the camera and returns it in PIL format
    def get_image():
     # read is the easiest way to get a full image out of a VideoCapture object.
     retval, im = camera.read()
     return im

    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
    for i in range(ramp_frames):
     temp = get_image()
    print("Taking image...")
    # Take the actual image we want to keep
    camera_capture = get_image()
    file = "imgconvert.jpg"
    # A nice feature of the imwrite method is that it will automatically choose the
    # correct format based on the file extension you provide. Convenient!
    cv2.imwrite(file, camera_capture)

    # You'll want to release the camera, otherwise you won't be able to create a new
    # capture object until your script exits
    del(camera)

def convert():
    img = PIL.Image.open('imgconvert.jpg')
    img = img.convert('L')
    img.save('image1.jpg')

    text = pytesseract.image_to_string(PIL.Image.open('image1.jpg'))
    print(text)

    f=open("output.txt","w")
    f.write(text)

def speech():
    f=open("output.txt","r")
    tts=f.read()
    tt= gTTS(tts,lang='en')
    tt.save("good.mp3")
    os.system(" good.mp3")

def exit():
    root.destroy()

root=Tk()
root.geometry('400x300')

lab=Label(root,
         text="WELCOME TO PYTHON",
         fg = "red",
         font = "Times 17 underline")
lab.pack()

lab=Label(root,
         text="PROJECT : IMAGE TO SPEECH CONVERTER",
         fg = "red",
         font = "Times")
lab.place(x=50,y=40)

lab1=Label(root,
         text="CAPTURE IMAGE : -",
         fg = "black",
         font = "Times")
lab1.place(x=70,y=100)

but1=Button(root,text="CAPTURE",command=cam)
but1.place(x=220,y=100)

lab1=Label(root,
         text="IMAGE TO TEXT : -",
         fg = "black",
         font = "Times")
lab1.place(x=70,y=150)

but1=Button(root,text="CONVERT",command=convert)
but1.place(x=220,y=150)

lab1=Label(root,
         text="TEXT TO SPEECH : -",
         fg = "black",
         font = "Times")
lab1.place(x=70,y=200)

but1=Button(root,text="SPEECH",command=speech,relief='raised')
but1.place(x=220,y=200)

button=Button(root,text="EXIT",relief='raised',font="Times",command=exit)
button.place(x=170,y=250)
#lab1.grid(row=0,sticky='e')

root.mainloop()
