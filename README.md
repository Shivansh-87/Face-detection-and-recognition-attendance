# 📸 Face Detection & Recognition Attendance System

An automated **attendance management system** built with Python, OpenCV, and the `face_recognition` library. The system detects faces in real time via webcam, recognizes registered individuals, and automatically marks their attendance — saving everything to an Excel/CSV file.

---

## 🚀 Features

- Real-time face detection using **webcam / camera**
- Recognizes known/registered faces automatically
- Marks attendance with **name + timestamp** on recognition
- Saves attendance records to **Excel / CSV** file
- Prevents duplicate entries for the same person in one session
- Simple to add new faces to the system

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.x |
| Face Detection | OpenCV (`cv2`) |
| Face Recognition | `face_recognition` (dlib-based) |
| Data Storage | CSV / Excel (`openpyxl` / `pandas`) |
| Camera Input | OpenCV VideoCapture |

---

## 📁 Project Structure

```
Face-detection-and-recognition-attendance/
├── known_faces/          # Store registered face images here (one per person)
│   ├── John.jpg
│   ├── Jane.jpg
│   └── ...
├── attendance/           # Auto-generated attendance files
│   └── Attendance_2024-01-01.csv
├── main.py               # Main script — run this to start
├── encode_faces.py       # Encodes known faces for recognition
├── requirements.txt
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.7+
- Webcam / camera
- `cmake` installed (required by dlib)

### Installation

```bash
# Clone the repository
git clone https://github.com/Shivansh-87/Face-detection-and-recognition-attendance.git
cd Face-detection-and-recognition-attendance

# Install dependencies
pip install -r requirements.txt
```

### requirements.txt

```
opencv-python
face_recognition
numpy
pandas
openpyxl
```

> **Note:** `face_recognition` requires `dlib`. On Windows, install Visual Studio Build Tools first. On Linux/Mac it installs automatically.

---

## 🏃 How to Use

### Step 1 — Add known faces

Place one clear photo of each person inside the `known_faces/` folder. Name each file after the person:

```
known_faces/
├── Rahul.jpg
├── Priya.jpg
└── Amit.jpg
```

### Step 2 — Run the system

```bash
python main.py
```

- The webcam will open
- When a recognized face appears, their name and timestamp are logged
- Press **`q`** to quit

### Step 3 — View attendance

Attendance is saved automatically to the `attendance/` folder as a CSV file named by today's date:

```
Name, Time
Rahul, 09:05:32
Priya, 09:07:14
```

---

## 📊 Attendance Output (CSV)

| Name | Time |
|---|---|
| Rahul | 09:05:32 |
| Priya | 09:07:14 |
| Amit | 09:12:45 |

---

## ⚠️ Troubleshooting

| Issue | Fix |
|---|---|
| `dlib` install fails | Install `cmake` and Visual Studio Build Tools (Windows) |
| Webcam not opening | Check camera index — try `cv2.VideoCapture(1)` |
| Face not recognized | Use a clearer, well-lit photo in `known_faces/` |
| Low accuracy | Ensure good lighting and a front-facing photo |

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is licensed under the MIT License.
