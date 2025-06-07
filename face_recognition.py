from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and Resize First Image
        img1 = Image.open("college_images/model-info-img.png")
        img1 = img1.resize((650, 700), Image.Resampling.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Place First Image
        bg_img1 = Label(self.root, image=self.photoimg1)
        bg_img1.place(x=0, y=45, width=650, height=700)

        # Load and Resize Second Image
        img2 = Image.open("college_images/Untitled-design-48.png")
        img2 = img2.resize((950, 700), Image.Resampling.LANCZOS)  
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Place Second Image
        bg_img2 = Label(self.root, image=self.photoimg2)
        bg_img2.place(x=650, y=45, width=950, height=700)

        b6_1 = Button(bg_img2, text="Face recognition", cursor="hand2", 
                    font=("times new roman", 20, "bold"), bg="darkblue", fg="white",command=self.face_recog)
        b6_1.place(x=365, y=547, width=200, height=40)

        #attendance======================================

        def mark_attendance(self, i, r, n, d):
            try:
                with open("jaadu.csv", "r+", newline="\n") as f:
                    myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    entry = line.strip().split(",")
                nameList.append(entry[0])  # Checking only Student_id
                if i not in nameList:
                    now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
            except Exception as e:
                messagebox.showerror("Error", f"Error while marking attendance: {str(e)}")



        # def mark_attendance(self,i,r,n,d):
        #     with open("jaadu.csv", "r+", newline="\n") as f:
        #         myDataList = f.readlines()
        #         nameList = []
        #         for line in myDataList:
        #             entry = line.split((","))
        #             nameList.append(entry[0])
        #         if ((i not in nameList) and (r not in nameList) and (n not in nameList) and (d not in nameList)):
        #             now = datetime.now()
        #             d1 = now.strftime("%d/%m/%Y")
        #             dtString = now.strftime("%H:%M:%S")
        #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present") 

            







        #face reco==================

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", user="root", password="jaiho123@#", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id = %s", (id,))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id = %s", (id,))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id = %s", (id,))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id = %s", (id,))
                i = my_cursor.fetchone()
                i = str(i[0]) if i else "Unknown"


                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord.append((x, y, w, h))
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 0, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()




    
        



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
