import tkinter as tk
import customtkinter as ctk
import torch
import numpy as np
import cv2
from playsound import playsound
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("600x600")
app.title("Drowsiness Detection App")
ctk.set_appearance_mode("dark")

Frame = tk.Frame(height = 450, width= 600)
Frame.pack()
vid = ctk.CTkLabel(Frame)
vid.pack()

counter = 0
counterLabel = ctk.CTkLabel(app, text = counter, height = 40, width = 120, text_color = "black", fg_color="cyan")
counterLabel.pack()

def counter_reset():
    global counter
    counter = 0
resetButton = ctk.CTkButton(app, text = "Reset Counter", command = counter_reset, height = 40, width = 120, text_color = "white", fg_color="cyan")
resetButton.pack()

model = torch.hub.load('ultralytics/yolov5', 'custom', path = 'yolov5/runs/train/exp3/weights/best.pt', force_reload=True)
cap = cv2.VideoCapture(0)
def detect():
    global counter
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame)
    img = np.squeeze(results.render())

    if len(results.xywh[0])>0:
        dconf = results.xywh[0][0][4]
        dclass = results.xywh[0][0][5]

        if dconf.item() > 0.89 and dclass.item() == 16.0:
            playsound("alerttone3.mp3")
            counter += 1

    imgarr = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(imgarr)
    vid.imgtk = imgtk
    vid.configure(image = imgtk)
    vid.after(10, detect)
    counterLabel.configure(text = counter)

detect()
app.mainloop()