from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from tkinter import messagebox
import tkinter.messagebox

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open(r"C:\Users\shiva\OneDrive\Desktop\frams\college_images\WhatsApp Image 2024-12-23 at 11.30.23_a85cbc12.jpg")
        img = img.resize((510, 150), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=510, height=150)

        # Second image
        img1 = Image.open(r"C:\Users\shiva\OneDrive\Desktop\frams\college_images\download.jpg")
        img1 = img1.resize((510, 150), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=510, y=0, width=510, height=150)

        # Third image
        img2 = Image.open(r"college_images/WhatsApp Image 2025-02-14 at 12.02.35_259fe095.jpg")
        img2 = img2.resize((510, 150), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1020, y=0, width=510, height=150)

        # Fourth background image
        img3 = Image.open(r"C:\Users\shiva\OneDrive\Desktop\frams\college_images\WhatsApp Image 2024-12-23 at 11.30.23_6d7e79c3.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1530, height=710)

        # Title Label
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)  # Set width to fit the screen, height for title visibility
        
        # Person button
        img4 = Image.open(r"college_images/WhatsApp Image 2025-02-14 at 11.57.29_91274a9b.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.Student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Person Details",command=self.Student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect face button
        img5 = Image.open(r"college_images/WhatsApp Image 2025-02-14 at 11.57.29_5dc56eac.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)



        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data ,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # Attendance button
        img6 = Image.open(r"C:\Users\shiva\OneDrive\Desktop\frams\college_images\WhatsApp Image 2025-02-14 at 11.57.29_e417d941.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Help button
        img7 = Image.open(r"C:\Users\shiva\OneDrive\Desktop\frams\college_images\WhatsApp Image 2025-02-14 at 11.59.42_bf104a31.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg7 = ImageTk.PhotoImage(img7)  # Fixed the assignment to the correct image

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)

        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # Train face buttonjpg
        img8 = Image.open("college_images/WhatsApp Image 2025-02-14 at 11.57.30_e5545e0e.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg8 = ImageTk.PhotoImage(img8)  # Fixed the assignment to the correct image

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b5.place(x=200, y=380, width=220, height=220)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=200, y=580, width=220, height=40)

        # photos face button
        img9 = Image.open("college_images/WhatsApp Image 2025-02-14 at 11.57.30_48c2d5d7.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg9 = ImageTk.PhotoImage(img9)  # Fixed the assignment to the correct image

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b6.place(x=500, y=380, width=220, height=220)

        b6_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=580, width=220, height=40)

        # Developer button
        img10 = Image.open(r"C:\Users\shiva\OneDrive\Desktop\frams\college_images\WhatsApp Image 2024-12-23 at 11.30.22_b290f30b.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg10 = ImageTk.PhotoImage(img10)  # Fixed the assignment to the correct image

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)

        b7_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=800, y=580, width=220, height=40)

        # Exit face button
        img11 = Image.open("college_images/WhatsApp Image 2025-02-14 at 11.59.43_c47ddcb9.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)  # Using LANCZOS instead of ANTIALIAS
        self.photoimg11 = ImageTk.PhotoImage(img11)  # Fixed the assignment to the correct image

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b8.place(x=1100, y=380, width=220, height=220)

        b8_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

        #=========function buttons==========

    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)   

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


