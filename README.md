README file for File_Read & Write Challenge project.

---

# 📂 File Read & Write Challenge

## 🖋️ Overview

This Python program reads the contents of a file provided by the user, modifies the content (converts it to **uppercase**), and writes the modified version to a new file.

It also includes error handling to gracefully manage common issues like missing files or permission errors.

---

## ⚙️ Features

* ✅ Reads text from a file.
* ✅ Converts the text to **uppercase**.
* ✅ Writes the modified content to a **new file** (prefixed with `modified_`).
* ✅ Handles errors:

  * File not found.
  * Permission denied.
  * Unexpected errors.

---

## 🚀 How to Run

1. Clone or download the project.
2. Make sure you have **Python 3** installed.
3. Place a text file (e.g., `input.txt`) in the same directory.
4. Run the program:

```bash
python file_read_write.py
```

5. When prompted, enter the filename you want to read (e.g., `input.txt`).
6. The program will create a new file (e.g., `modified_input.txt`) containing the modified content.

---

## 📌 Example

**input.txt**

```
Hello world!
This is a test file.
```

**modified\_input.txt**

```
HELLO WORLD!
THIS IS A TEST FILE.
```

---

## 🧪 Error Handling Lab

* If the file doesn’t exist → `"❌ Error: The file was not found."`
* If there’s no permission → `"❌ Error: You don’t have permission to read this file."`
* If another issue occurs → Displays the unexpected error message.
