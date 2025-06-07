from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="Developer", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and Resize Top Image
        img_top = Image.open("college_images/face-detection-example.jpg")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)  
        self.photoimg_top_bg = ImageTk.PhotoImage(img_top)

        # Place Image
        bg_img_top = Label(self.root, image=self.photoimg_top_bg)
        bg_img_top.place(x=0, y=45, width=1530, height=720)

        #==================Main Frame================

        main_frame = Frame(bg_img_top, bd=2, bg="white")
        main_frame.place(x=400, y=100, width=700, height=400)  # Adjusted center position

        # Load and resize the three images
        img1 = Image.open("college_images/WhatsApp Image 2025-04-26 at 21.46.29_2cbd8eb8.jpg")
        img1 = img1.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img2 = Image.open("college_images/WhatsApp Image 2025-04-26 at 21.43.48_4d100462.jpg")
        img2 = img2.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img3 = Image.open("college_images/WhatsApp Image 2025-04-26 at 21.42.04_8e56b70c.jpg")  # Replace with another image if needed
        img3 = img3.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Image 1
        img_label1 = Label(main_frame, image=self.photoimg1, bg="white")
        img_label1.grid(row=0, column=0, padx=10, pady=10)

        caption1 = Label(main_frame, text="Shivansh", font=("times new roman", 14, "bold"), bg="white")
        caption1.grid(row=1, column=0, pady=5)

        # Image 2
        img_label2 = Label(main_frame, image=self.photoimg2, bg="white")
        img_label2.grid(row=0, column=1, padx=10, pady=10)

        caption2 = Label(main_frame, text="Pranjali", font=("times new roman", 14, "bold"), bg="white")
        caption2.grid(row=1, column=1, pady=5)

        # Image 3
        img_label3 = Label(main_frame, image=self.photoimg3, bg="white")
        img_label3.grid(row=0, column=2, padx=10, pady=10)

        caption3 = Label(main_frame, text="Prashant", font=("times new roman", 14, "bold"), bg="white")
        caption3.grid(row=1, column=2, pady=5)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
