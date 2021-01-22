import tkinter
import cv2
import PIL.Image , PIL.ImageTk
from functools import partial
import threading
import time
import imutils

stream = cv2.VideoCapture("vedio.mp4")
flag = True
def pending(decision):

    #Decision Pending

    frame = cv2.cvtColor(cv2.imread("dp.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = WIDTH,height = HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame,anchor = tkinter.NW)

    time.sleep(1.5)

    frame = cv2.cvtColor(cv2.imread("drs dhoni.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = WIDTH,height = HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame,anchor = tkinter.NW)

    time.sleep(2.5)

    if decision == 'out':
        decisionImg = "out.jpg"

    else:
        decisionImg = "not_out.jpg"

    frame = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = WIDTH,height = HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame,anchor = tkinter.NW)



def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    thread = threading.Thread(target=pending,args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")





def play(speed):
    global flag
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed , frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame,width = WIDTH,height = HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) #Tkinter compatibility
    canvas.image = frame
    canvas.create_image(0,0,image = frame,anchor = tkinter.NW)

    if flag:
        canvas.create_text(120,75,fill = "black",font = "Times 20 bold", text = "Decision Pending")
    flag = not flag
    


    
    


WIDTH = 650
HEIGHT = 368


window = tkinter.Tk()
window.title("DRS-- DHONI REVIEW SYSTEM")


cv_img = cv2.cvtColor(cv2.imread("home.jpg"),cv2.COLOR_BGR2RGB)

canvas = tkinter.Canvas(window,width=WIDTH,height=HEIGHT)

photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image = photo)

canvas.pack()


#Buttons to control PlayBack

btn = tkinter.Button(window,text = "<< PREVIOUS(FAST)",width = 50,command = partial(play,-25))
btn.pack()
btn = tkinter.Button(window,text = "<< PREVIOUS(SLOW)",width = 50,command = partial(play,-2))
btn.pack()
btn = tkinter.Button(window,text = "NEXT(FAST) >> ",width = 50,command = partial(play,25))
btn.pack()
btn = tkinter.Button(window,text = "NEXT(SLOW) >> ",width = 50,command = partial(play,2))
btn.pack()
btn = tkinter.Button(window,text = "OUT !",width = 50 , command = out)
btn.pack()
btn = tkinter.Button(window,text = "NOT OUT !",width = 50,command = not_out)
btn.pack()

window.mainloop()