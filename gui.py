# CompuTask v0.6
import json
import os
import tkinter as tk 
from tkinter import messagebox

arquivo = "tarefas.json"
tarefas = []
filtro_atual = "todas"

# Janela principal
janela = tk.Tk()
janela.title("CompuTask")
janela.geometry("400x450")

# Titulo
titulo = tk.Label(janela, text="CompuTask v0.6", font=("Arial", 16)) 
titulo.pack(pady=10)

# Status
status_texto = tk.StringVar()
status_texto.set("Nenhuma tarefa ainda")
status = tk.Label(janela, textvariable=status_texto, font=("Arial", 10), fg="gray")
status.pack(pady=5)

# Campo para digitar
entrada_tarefa = tk.Entry(janela)
entrada_tarefa.pack(fill="x", padx=10, pady=5)

# Lista de tarefas
lista = tk.Listbox(janela)
lista.pack(expand=True, fill="both", padx=10, pady=10)

# Funções
def adicionar_tarefa():
    texto = entrada_tarefa.get().strip()
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
    atualizar_lista()
    atualizar_status()

def atualizar_status():
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t["concluida"])
    ativas = total - concluidas
    status_texto.set(f"{ativas} ativa(s) • {concluidas} concluída(s)")

def atualizar_lista():
    lista.delete(0, tk.END)
    for tarefa in tarefas:
        texto = tarefa["texto"]
        concluida = tarefa["concluida"]
        prefixo = "🗹" if concluida else "☐"
        lista.insert(tk.END, prefixo + texto)

def salvar_tarefas(tarefas):
    with open (arquivo, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

def carregar_json():
    global tarefas
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
        tarefas = []
        for item in dados:
            if isinstance(item, dict):
                tarefas.append(item)
            else:
                tarefas.append({"texto": str(item), "concluida": False})
    
def mudar_filtro(novo_filtro):
    global filtro_atual
    filtro_atual = novo_filtro
    atualizar_lista()

def ao_selecionar_tarefa(event):
    selecionado = lista.curselection()
    if not selecionado:
        return
    indice = selecionado[0]
    tarefa = tarefas[indice]
    concluida_var = tk.BooleanVar
    concluida_var.set(tarefa["concluida"])
    lista.bind("<<ListboxSelect>>", ao_selecionar_tarefa)

# Botões
botao_add = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa) 
botao_add.pack(pady=2)

botao_concluir = tk.Button(janela, text="(Des)concluir tarefa", command=concluir_tarefa)
botao_concluir.pack(pady=2)

botao_excluir = tk.Button(janela, text="Excluir tarefa", command=excluir_tarefa)
botao_excluir.pack(pady=2)

frame_filtros = tk.Frame(janela)
frame_filtros.pack(pady=5)
btn_todas = tk.Button(frame_filtros, text="Todas", command=lambda: mudar_filtro("todas"))
btn_todas.pack(side="left", padx=5)
btn_ativas = tk.Button(frame_filtros, text="Ativas", command=lambda: mudar_filtro("ativas"))
btn_ativas.pack(side="left", padx=5)
btn_concluidas = tk.Button(frame_filtros, text="Concluídas", command=lambda: mudar_filtro("concluidas"))
btn_concluidas.pack(side="left", padx=5)

# Loop da Janela
atualizar_lista()
atualizar_status()

janela.mainloop()