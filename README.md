# 📋 ClipHistory - A Lightweight Clipboard Manager

A simple, cross-platform clipboard manager built with Python and Tkinter. It runs in the background and saves a running history of your copied text, so you never lose an important link or piece of text again.

<img width="675" height="873" alt="image" src="https://github.com/user-attachments/assets/253c612a-8a21-4095-9a56-5a3497c5a602" />

---

## 🚀 Features

- **Clipboard Monitoring:** Automatically detects and saves new text copied to the clipboard.
- **History List:** Displays a clean, scrollable list of your last 20 copied items.
- **Instant Restore:** Simply click any item in the list to instantly copy it back to your clipboard.
- **Smart Preview:**
  - Truncates long, multi-line snippets to a 3-line preview.
  - Intelligently wraps and truncates very long single lines to keep the UI clean.
- **Lightweight:** Uses minimal CPU and RAM, running efficiently in the background.

---

## 🛠️ Built With

- **Python 3:** The core programming language.
- **Tkinter:** For the simple, cross-platform graphical user interface (GUI).
- **Pyperclip:** A cross-platform module for clipboard access.
- **Textwrap:** A standard library for formatting text previews.
- **PyInstaller:** To package the script into a standalone `.exe` for Windows.

---

## 💻 How to Run (For Developers)

To run this project from the source code, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/GegarinSagolsem/Clip-History.git](https://github.com/GegarinSagolsem/Clip-History.git)
    cd Clip-History
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # Create the environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Create and install requirements:**
    (install the packages)

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python src/main.py
    ```

---

## 📦 How to Build the `.exe`

To package the application into a standalone `.exe` file for Windows:

1.  **Install PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

2.  **Run the build command:**

    ```bash
    pyinstaller --onefile --windowed --name ClipHistory src/main.py
    ```

3.  **Find your app:**
    The finished `ClipHistory.exe` will be inside the new `dist` folder.
