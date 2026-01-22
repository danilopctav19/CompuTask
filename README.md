<p align="center">
  <img src="./assets/logo.png" alt="CompuTask logo" width="96">
</p>

# CompuTask

**CompuTask is a simple, lightweight, and honest task manager - built for modest computers and real people.**

---

## ✨ What is CompuTask?

CompuTask is a task list application focused on simplicity, performance, and local control.

It was created to run well on older or low-spec computers, without relying on internet access, online accounts, artificial intelligence, or cloud services.

Here, a task is just a task.

---

## 🎯 Who is it for?

CompuTask is for people who:

- Use older or low-end computers
- Prefer simple and straightforward software
- Do not want accounts or cloud synchronization
- Value privacy and local data control
- Want a program that **just works**, without distractions

---

## 🚫 What CompuTask is not trying to be

CompuTask is **not**:

- An AI-powered application
- An online service
- A corporate project management tool
- A product with ads or tracking
- A platform that collects your data

It does not try to compete with everything.  
It only tries to be useful.

---

## 🖥️ Compatibility

CompuTask was designed to run in simple environments and works well on:

- Windows
- Linux (especially lightweight distributions)

No heavy requirements. No unnecessary dependencies. Designed to respect older hardware

---

## 🔒 Privacy

CompuTask works with local data.

- No account required
- No data is sent to the internet
- No information is collected

Your data stays with you.

---

## 📦 Project status

**Version:** CompuTask 0.9 Beta  

The project is under active development and may receive improvements, while prioritizing stability, simplicity, and compatibility.

---

## 📜 License

This project is distributed under the license described in the `LICENSE` file.

---

## ❤️ Philosophy

CompuTask is built on a simple idea:

> Not every computer is new.  
> Not every user wants complexity.  
> And software can still be simple, useful, and respectful.

---

## 🧩 Dependency: Tkinter

CompuTask uses Tkinter, which is the standard graphics library for Python.

In some Linux distributions, Tkinter is not installed by default, even with Python installed.

If the application does not open or shows an error related to Tkinter, follow the instructions below.

## 🐧 Linux

🔹 Debian / Ubuntu / Linux Mint / Pop!_OS / Xubuntu / Lubuntu:
sudo apt update
sudo apt install python3-tk

🔹 Fedora / Nobara / RHEL / CentOS / Rocky Linux:
sudo dnf install python3-tkinter

🔹 Arch Linux / Manjaro / EndeavourOS:
sudo pacman -S tk

🔹 openSUSE:
sudo zypper install python3-tk

## ✅ How to test if Tkinter is working
In terminal:
python3 - <<EOF
import tkinter as tk
tk.Tk()
print("Tkinter OK!")
EOF
Se uma janelinha abrir, está tudo certo ✔️

## 📦 AppImage and Tkinter

⚠️ Important
Even when using AppImage, Tkinter depends on system graphics libraries (X11 / Wayland).

Therefore, Tkinter must be installed on the host system.

This is normal for Tk-based applications.

🧠 Why does this happen?

Python comes pre-installed.
Tkinter is packaged separately.
Some distributions choose not to install graphical components by default.

