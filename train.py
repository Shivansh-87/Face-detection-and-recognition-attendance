from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="Train Data Set", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and Resize Top Image
        img_top = Image.open("college_images/face-detection-example.jpg")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)  
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Place Image
        bg_img_top = Label(self.root, image=self.photoimg_top)
        bg_img_top.place(x=0, y=45, width=1530, height=325)

        # Train Button
        b6_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", 
                    font=("times new roman", 30, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=0, y=380, width=1530, height=63)

        # Load and Resize Bottom Image
        img_bottom = Image.open("college_images/opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)  
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # Place Image
        bg_img_bottom = Label(self.root, image=self.photoimg_bottom)
        bg_img_bottom.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"

        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!")
            return

        paths = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".jpg") or f.endswith(".png")]
        
        if len(paths) == 0:
            messagebox.showerror("Error", "No images found in dataset!")
            return

        faces = []
        ids = []

        for image_path in paths:
            try:
                img = Image.open(image_path).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')

                # Extract ID from filename (assuming format "user.id.anything.jpg")
                id = int(os.path.split(image_path)[1].split('.')[1])
                faces.append(imageNp)
                ids.append(id)

                # Display the training image
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)

            except Exception as e:
                print(f"Error processing {image_path}: {e}")

        ids = np.array(ids)

        # Train the classifier
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training dataset completed successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to train the model: {e}")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()



