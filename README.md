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

**Version:** CompuTask 0.7 Beta  

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

---- ⬇️ In portuguese ----

## 🧩 Dependência: Tkinter

O CompuTask utiliza Tkinter, que é a biblioteca gráfica padrão do Python.
Em algumas distribuições Linux, o Tkinter não vem instalado por padrão, mesmo com o Python instalado.
Se o aplicativo não abrir ou mostrar erro relacionado a tkinter, siga as instruções abaixo.

## 🐧 Linux

🔹 Debian / Ubuntu / Linux Mint / Pop!_OS / Xubuntu / Lubuntu
Bash:
sudo apt update
sudo apt install python3-tk

🔹 Fedora / Nobara / RHEL / CentOS / Rocky Linux
Bash
sudo dnf install python3-tkinter

🔹 Arch Linux / Manjaro / EndeavourOS
Bash
sudo pacman -S tk

🔹 openSUSE
Bash
sudo zypper install python3-tk

## ✅ Como testar se o Tkinter está funcionando
No terminal:
Copiar código
Bash
python3 - <<EOF
import tkinter as tk
tk.Tk()
print("Tkinter OK!")
EOF
Se uma janelinha abrir, está tudo certo ✔️

## 📦 AppImage e Tkinter

⚠️ Importante
Mesmo usando AppImage, o Tkinter depende de bibliotecas gráficas do sistema (X11 / Wayland).
Por isso, é necessário que o Tkinter esteja instalado no sistema hospedeiro.
Isso é normal para aplicações baseadas em Tk.

🧠 Por que isso acontece?
O Python vem instalado
O Tkinter é empacotado separadamente
Algumas distros optam por não instalar componentes gráficos por padrão
