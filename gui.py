# CompuTask v1.0
import json
import sys
import os
import tkinter as tk 
from tkinter import PhotoImage
from tkinter import messagebox

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

arquivo = "tarefas.json"
tarefas = []
janela = tk.Tk()
janela.withdraw()

# Janela principal
splash = tk.Toplevel()
splash.title("CompuTask 1.0")
splash.geometry("300x150")
splash.resizable(False, False)

icon_path = "assets/logo_64x64.png"
icon = tk.PhotoImage(file=resource_path("assets/logo_64x64.png"))
splash.iconphoto(False, icon)

status = tk.Label(
    splash,
    text="Carregando CompuTask...",
    fg="gray",
    font=("Segoe UI", 11)
)
status.pack(expand=True)

# Titulo
titulo = tk.Label(janela, text="CompuTask v0.9", font=("Arial", 16)) 
titulo.pack(pady=10)

# Entrada de texto
entrada_tarefa = tk.Entry(janela)
entrada_tarefa.pack(fill="x", padx=10)

# Status
status_texto = tk.StringVar()
status_texto.set("Nenhuma tarefa ainda")
status = tk.Label(janela, textvariable=status_texto, font=("Arial", 10), fg="gray")
status.pack(pady=5)

# Funções
def montar_interface():
    global lista, entrada_tarefa

    janela.title("CompuTask")
    janela.geometry("400x450")
    janela.resizable(False, False)

    lista = tk.Listbox(janela)
    lista.pack(fill="both", expand=True, padx=10, pady=10)

    btn_add = tk.Button(janela, text="Adicionar", command=adicionar_tarefa)
    btn_add.pack(pady=5)

    btn_con = tk.Button(janela, text="(Des)concluir", command=concluir_tarefa)
    btn_con.pack()

    btn_del = tk.Button(janela, text="Excluir", command=excluir_tarefa)
    btn_del.pack()

    carregar_tarefas()
    for t in tarefas:
        lista.insert(tk.END, t)

    atualizar_lista()

def adicionar_tarefa():
    texto = entrada_tarefa.get()
    if not texto:
        return
    tarefas.append({"texto": texto, "concluida": False})
    lista.insert(tk.END, texto)
    entrada_tarefa.delete(0, tk.END)
    atualizar_lista()
    atualizar_status()
    salvar_tarefas()

def concluir_tarefa():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa.")
        return
    indice = selecionado[0]
    tarefas[indice] ["concluida"] = not tarefas[indice]["concluida"]
    atualizar_lista()
    atualizar_status()
    salvar_tarefas()

def excluir_tarefa():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para excluir.")
        return
    if not messagebox.askyesno("Confirmar", "Excluir esta tarefa?"):
        return
    indice = selecionado[0]
    del tarefas[indice]
    salvar_tarefas()
    atualizar_lista()
    atualizar_status()

def atualizar_status():
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t["concluida"])
    ativas = total - concluidas
    status_texto.set(f"{ativas} ativa(s) • {concluidas} concluída(s)")

def carregar_tarefas():
    global tarefas
    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r") as f:
                tarefas = json.load(f)
        except:
            tarefas = []
    else:
        tarefas = []


def salvar_tarefas():
    with open (arquivo, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

def atualizar_lista():
    lista.delete(0, tk.END)
    for tarefa in tarefas:
        texto = tarefa["texto"]
        concluida = tarefa["concluida"]
        prefixo = "🗹" if concluida else "☐"
        lista.insert(tk.END, prefixo + texto)

def iniciar_app():
    splash.destroy()
    janela.deiconify()
    montar_interface()

# Loop da Janela
carregar_tarefas()
atualizar_status()
splash.after(800, iniciar_app)

janela.mainloop()
