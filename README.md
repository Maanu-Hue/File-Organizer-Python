# 📂 File Organizer using Python

A simple Python automation script that organizes files in a directory into categorized folders based on file type.

---

## 🚀 Features

* Automatically sorts files into folders:

  * 📊 Excel Files (`.xlsx`)
  * 🖼️ Image Files (`.jpg`, `.jpeg`, `.png`)
  * 🌐 WebP Files (`.webp`)
  * 📝 Text Files (`.txt`)
* Creates folders if they don't exist
* Skips unsupported file types safely
* Helps keep your workspace clean and organized

---

## 🛠️ Technologies Used

* Python
* Built-in modules:

  * `os`
  * `shutil`

---

## 📁 Project Structure

```
FILE_PYTHON/
│
├── Excel file/
├── Image file/
├── webp file/
├── Text file/
│
└── Files_Automated.py
```

---

## ⚙️ How It Works

1. Reads all files from the given directory
2. Checks file extensions
3. Creates folders if needed
4. Moves files into appropriate folders

---

## 🧠 Code Overview

```python
import os, shutil

path = r"C:/Users/manas/OneDrive/Desktop/FILE_PYTHON/"
og_files = os.listdir(path)

file_name = ['Excel file', 'Image file', 'webp file', 'Text file']

# Create folders if not exist
for loop in range(0, 4):
    pathname = os.path.join(path, file_name[loop])
    if not os.path.exists(pathname):
        os.makedirs(pathname)

# Move files
for file in og_files:
    source = os.path.join(path, file)

    if not os.path.isfile(source):
        continue

    if file.lower().endswith(".txt"):
        destination = os.path.join(path, "Text file", file)

    elif file.endswith(".xlsx"):
        destination = os.path.join(path, "Excel file", file)

    elif file.endswith(".webp"):
        destination = os.path.join(path, "webp file", file)

    elif file.endswith((".jpeg", ".jpg", ".png")):
        destination = os.path.join(path, "Image file", file)

    else:
        print("Not moved:", file)
        continue

    shutil.move(source, destination)
```

---

## 📸 Output Example

### Before Organizing

![Before](https://raw.githubusercontent.com/Maanu-Hue/File-Organizer-Python/a8e5bdfcd9599dfe417e08299c68a9ce7ee45ad8/Screenshot%202026-04-18%20162246.png)

### After Organizing

![After](https://raw.githubusercontent.com/Maanu-Hue/File-Organizer-Python/a8e5bdfcd9599dfe417e08299c68a9ce7ee45ad8/Screenshot%202026-04-18%20163851.png)

---

## 📌 How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/file-organizer-python.git
```

2. Open in VS Code or any IDE

3. Run the script:

```
python file_organizer.py
```

---

## ⚠️ Note

* Make sure to update the `path` variable according to your system.
* Avoid running on system folders (like `C:/Windows`).

---

## 🌟 Future Improvements

* Add GUI (Tkinter)
* Support more file types
* Add logging system
* Add undo feature

---

## 💡 Inspiration

This project is a beginner-friendly automation task to practice Python file handling and improve productivity.

---
