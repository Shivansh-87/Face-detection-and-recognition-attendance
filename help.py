from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="Help desk", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and Resize Top Image
        img_top = Image.open("college_images/service49_0.gif")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)  
        self.photoimg_top_bg = ImageTk.PhotoImage(img_top)

        # Place Image
        bg_img_top = Label(self.root, image=self.photoimg_top_bg)
        bg_img_top.place(x=0, y=45, width=1530, height=720)

        new_text = Label(bg_img_top, text="For any assistance, please contact:", font=("times new roman", 20), bg="white", fg="black")
        new_text.place(x=100, y=240)

        dev_info = Label(bg_img_top, text="Email: Shivansh@gmail.com", font=("times new roman", 18), bg="white", fg="black")
        dev_info.place(x=100, y=270)



if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()