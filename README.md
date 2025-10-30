# 📋 ClipHistory - A Lightweight Clipboard Manager

A simple, cross-platform (Windows & Linux) clipboard manager built with Python and Tkinter. It runs in the background and saves a running history of your copied text, so you never lose an important link or piece of text again.

<img width="675" height="873" alt="image" src="https://github.com/user-attachments/assets/253c612a-8a21-4095-9a56-5a3497c5a602" />

---

## ⚡ Quick Download

The easiest way to get the app is to download the pre-built version for your system.

**Go to the [Releases Page](https://github.com/GegarinSagolsem/Clip-History/releases)**

<img width="1465" height="815" alt="image" src="https://github.com/user-attachments/assets/7c23912e-53e2-4791-961c-68759655ea6b" />


- For **Windows**: Download `ClipHistory.exe`
- For **Linux**: Download `ClipHistory` (you may need to [make it executable](https://github.com/GegarinSagolsem/Clip-History#how-to-run-for-developers) after downloading).

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
- **PyInstaller:** To package the script into a standalone executable.

---

## 💻 How to Run (For Developers)

To run this project from the source code, follow these steps:

1.  **Clone the repository:**

    ```bash
    https://github.com/GegarinSagolsem/Clip-History.git
    cd Clip-History
    ```

2.  **Install System Dependencies (Linux Only!):**
    On Linux (especially Debian/Ubuntu/Kali), you must install `tkinter` and `xclip` at the system level:

    ```bash
    sudo apt update
    sudo apt install python3-tk python3-venv xclip
    ```

3.  **Create and activate a virtual environment:**

    ```bash
    # Create the environment (use python3 on Linux)
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

4.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application:**

    ```bash
    # Use python on Windows
    python src/main.py

    # Use python3 on Linux
    python3 src/main.py
    ```

---

## 📦 How to Build (from Source)

To package the application into a standalone file yourself:

1.  **Install PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

2.  **Run the build command:**

    - **On Windows (in PowerShell/CMD):**

      ```bash
      pyinstaller --onefile --windowed --name ClipHistory src/main.py
      ```

    - **On Linux (in Terminal):**
      ```bash
      pyinstaller --onefile --windowed --name ClipHistory src/main.py
      ```

3.  **Make the Linux version executable:**

    ```bash
    chmod +x dist/ClipHistory
    ```

4.  **Find your app:**
    The finished executable will be inside the `dist` folder.
