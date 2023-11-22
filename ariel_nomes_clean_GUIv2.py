import tkinter as tk
from tkinter import messagebox, ttk
from random import choice
from os import startfile
from PIL import Image, ImageTk

FONT = ("Arial", 12)

root = tk.Tk()
root.config(height=400, width=400, pady=20, padx=20)
root.resizable(width=False, height=False)
root.title("GERADOR DE NOMES ALEATÓRIOS")

nomes_mas = []
nomes_fem = []
sobrenomes = []

def ler_arquivo(arquivo):
    with open(arquivo) as file:
        lista = file.readlines()
        lista = [nome.rstrip("\n") for nome in lista]
        if len(lista[0]) == 0:
            lista = [nome.rstrip("\n") for nome in lista[:-1]]
    return lista

nomes_mas = ler_arquivo("nomes_mas.txt")
nomes_fem = ler_arquivo("nomes_fem.txt")
sobrenomes = ler_arquivo("sobrenomes.txt")

nomes_lista = []
sobrenomes_lista = []
nome_sobrenome_anterior = []

def escrever_em_arquivo(arquivo, nome):
    with open(arquivo, mode="a") as file:
        file.write(f"\n{nome}")
        adicionar_entry.delete(0, "end")
    return ler_arquivo(arquivo)

def remover_nome_no_arquivo(arquivo, lista, nome_deletar):
    with open(arquivo, "w") as file:
        for nome in lista:
            if nome == lista[0] and nome != nome_deletar:
                file.write(nome)
            elif nome != lista[0] and nome != nome_deletar:
                file.write(f"\n{nome}")
    adicionar_entry.delete(0, "end")
    return ler_arquivo(arquivo)

def escolha_feita():
    global escolha
    escolha = var.get()

def gerar_nome():
    global escolha
    global travar_nome_var
    global travar_sobrenome_var
    global nomes_lista
    global sobrenomes_lista
    if escolha == 1:
        if travar_sobrenome_var == False or travar_sobrenome_var == None:
            if travar_nome_var == True:
                if len(nomes_lista) < 1:
                    messagebox.showerror(message="Destrave a geração de nomes!")
                else:
                    if nomes_lista[-1] not in nomes_mas:
                        nomes_lista[-1] = choice(nomes_mas)
                    nome_travado = nomes_lista[-1]
                    if len(sobrenomes_lista) > 2:
                        sobrenomes_lista.remove(sobrenomes_lista[-3])
                    sobrenome = choice(sobrenomes)
                    sobrenomes_lista.append(sobrenome)
                    nome_gerado_lbl.config(text=f"{nome_travado} {sobrenome}")
            elif travar_nome_var == False or travar_nome_var == None:
                if len(nomes_lista) > 2:
                    nomes_lista.remove(nomes_lista[-3])
                nome = choice(nomes_mas)
                if len(sobrenomes_lista) > 2:
                    sobrenomes_lista.remove(sobrenomes_lista[-3])
                sobrenome = choice(sobrenomes)
                sobrenomes_lista.append(sobrenome)
                nomes_lista.append(nome)
                nome_gerado_lbl.config(text=f"{nome} {sobrenome}")
        else:
            if len(sobrenomes_lista) < 1:
                messagebox.showerror(message="Destrave a geração de sobrenomes!")
            else:
                if travar_nome_var == True:
                    messagebox.showerror(message="Impossível gerar nome com nome e sobrenome travados!")
                else:
                    nome = choice(nomes_mas)
                    sobrenome_travado = sobrenomes_lista[-1]
                    nome_gerado_lbl.config(text=f"{nome} {sobrenome_travado}")

    elif escolha == 2:
        if travar_sobrenome_var == False or travar_sobrenome_var == None:
            if travar_nome_var == True:
                if len(nomes_lista) < 1:
                    messagebox.showerror(message="Destrave a geração de nomes!")
                else:
                    if nomes_lista[-1] not in nomes_fem:
                        nomes_lista[-1] = choice(nomes_fem)
                    nome_travado = nomes_lista[-1]
                    if len(sobrenomes_lista) > 2:
                        sobrenomes_lista.remove(sobrenomes_lista[-3])
                    sobrenome = choice(sobrenomes)
                    sobrenomes_lista.append(sobrenome)
                    nome_gerado_lbl.config(text=f"{nome_travado} {sobrenome}")
            elif travar_nome_var == False or travar_nome_var == None:
                if len(nomes_lista) > 2:
                    nomes_lista.remove(nomes_lista[-3])
                nome = choice(nomes_fem)
                if len(sobrenomes_lista) > 2:
                    sobrenomes_lista.remove(sobrenomes_lista[-3])
                sobrenome = choice(sobrenomes)
                sobrenomes_lista.append(sobrenome)
                nomes_lista.append(nome)
                nome_gerado_lbl.config(text=f"{nome} {sobrenome}")
        else:
            if len(sobrenomes_lista) < 1:
                messagebox.showerror(message="Destrave a geração de sobrenomes!")
            else:
                if travar_nome_var == True:
                    messagebox.showerror(message="Impossível gerar nome com nome e sobrenome travados!")
                else:
                    nome = choice(nomes_fem)
                    sobrenome_travado = sobrenomes_lista[-1]
                    nome_gerado_lbl.config(text=f"{nome} {sobrenome_travado}")
    else:
        messagebox.showerror(message="Selecione um gênero para gerar o nome!")
    root.clipboard_clear()
    root.clipboard_append(nome_gerado_lbl.cget("text").strip())
    root.update()

def travar_nome():
    global travar_nome_var
    if travar_nome_var == True:
        travar_nome_var = False
        cadeado_nome_btn.config(image=cadeado_nome_icone)
    else:
        travar_nome_var = True
        cadeado_nome_btn.config(image=cadeado_nome_ativo_icone)

def travar_sobrenome():
    global travar_sobrenome_var
    if travar_sobrenome_var == True:
        travar_sobrenome_var = False
        cadeado_sobrenome_btn.config(image=cadeado_sobrenome_icone)
    else:
        travar_sobrenome_var = True
        cadeado_sobrenome_btn.config(image=cadeado_sobrenome_ativo_icone)

def exibir_nome_anterior():
    global nomes_lista
    global sobrenomes_lista
    if len(nomes_lista) > 0 and len(sobrenomes_lista) > 0:
        nome_anterior = nomes_lista[-2]
        sobrenome_anterior = sobrenomes_lista[-2]
        nome_gerado_lbl.config(text=f"{nome_anterior} {sobrenome_anterior}")
    elif len(nomes_lista) > 1 and len(sobrenomes_lista) > 1:
        nome_anterior = [nomes_lista][-2]
        sobrenome_anterior = [sobrenomes_lista][-2]
        nome_gerado_lbl.config(text=f"{nome_anterior} {sobrenome_anterior}")
    else:
        messagebox.showerror(message="Não há nome anterior gravado!")

def exibir_nome_atual():
    global nomes_lista
    global sobrenomes_lista
    if len(nomes_lista) > 0 and len(sobrenomes_lista) > 0:
        nome_atual = nomes_lista[-1]
        sobrenome_atual = sobrenomes_lista[-1]
        nome_gerado_lbl.config(text=f"{nome_atual} {sobrenome_atual}")
    elif len(nomes_lista) > 1 and len(sobrenomes_lista) > 1:
        nome_atual = [nomes_lista][-1]
        sobrenome_atual = [sobrenomes_lista][-1]
        nome_gerado_lbl.config(text=f"{nome_atual} {sobrenome_atual}")

def adicionar_nome():
    global escolha
    global nomes_mas
    global nomes_fem

    nome_para_adicionar = adicionar_entry.get().strip().title()

    if checar_vazio(nome_para_adicionar):
        messagebox.showerror(message="Campo vazio!")
    else:
        if escolha == 1:
            if checar_repetido(nome_para_adicionar, nomes_mas):
                messagebox.showerror(message=f"'{nome_para_adicionar}' já está presente na lista de nomes masculinos.")
            else:
                confirm = messagebox.askyesno(
                    message=f"Confirma adicionar nome masculino '{nome_para_adicionar}'?")
                if confirm:
                    nomes_mas = escrever_em_arquivo("nomes_mas.txt", nome_para_adicionar)

        elif escolha == 2:
            if checar_repetido(nome_para_adicionar, nomes_fem):
                messagebox.showerror(message=f"'{nome_para_adicionar}' já está presente na lista de nomes femininos.")
            else:
                confirm = messagebox.askyesno(message=f"Confirma adicionar nome feminino '{nome_para_adicionar}'?")
                if confirm:
                    nomes_fem = escrever_em_arquivo("nomes_fem.txt", nome_para_adicionar)

        else:
            messagebox.showerror(message="Selecione um gênero para adicionar o nome!")


def remover_nome():
    global nomes_mas
    global nomes_fem
    global sobrenomes

    nome_para_remover = adicionar_entry.get().strip().title()

    if nome_para_remover in nomes_mas:
        confirm_remover = messagebox.askyesno(message=f"'{nome_para_remover}' está presente na lista de nomes masculinos. Confirma a remoção?")
        if confirm_remover:
            nomes_mas = ler_arquivo("nomes_mas.txt")
            nomes_mas = remover_nome_no_arquivo("nomes_mas.txt", nomes_mas, nome_para_remover)

    elif nome_para_remover in nomes_fem:
        confirm_remover = messagebox.askyesno(message=f"'{nome_para_remover}' está presente na lista de nomes femininos. Confirma a remoção?")
        if confirm_remover:
            nomes_fem = ler_arquivo("nomes_fem.txt")
            nomes_fem = remover_nome_no_arquivo("nomes_fem.txt", nomes_fem, nome_para_remover)

    elif nome_para_remover in sobrenomes:
        confirm_remover = messagebox.askyesno(message=f"'{nome_para_remover}' está presente na lista de sobrenomes. Confirma a remoção?")
        if confirm_remover:
            sobrenomes = ler_arquivo("sobrenomes.txt")
            sobrenomes = remover_nome_no_arquivo("sobrenomes.txt", sobrenomes, nome_para_remover)

    else:
        messagebox.showerror(message=f"'{nome_para_remover}' não foi encontrado em nenhuma lista.")

def checar_vazio(nome):
    if len(nome) == 0:
        return True


def checar_repetido(nome, lista):
    if nome in lista:
        return True


def adicionar_sobrenome():
    global sobrenomes
    sobrenome_para_adicionar = adicionar_entry.get().strip().capitalize()

    if checar_vazio(sobrenome_para_adicionar):
        messagebox.showerror(message="Campo vazio!")
    else:
        if checar_repetido(sobrenome_para_adicionar, sobrenomes):
            messagebox.showerror(message=f"'{sobrenome_para_adicionar}' já está presente na lista de sobrenomes.")
        else:
            confirm = messagebox.askyesno(message=f"Confirma adicionar sobrenome '{sobrenome_para_adicionar}'?")
            if confirm:
                sobrenomes = escrever_em_arquivo("sobrenomes.txt", sobrenome_para_adicionar)


def abrir_nomes_mas_txt():
    startfile("nomes_mas.txt")

def abrir_nomes_fem_txt():
    startfile("nomes_fem.txt")

def abrir_sobrenomes_txt():
    startfile("sobrenomes.txt")


escolha = None
var = tk.IntVar()

masculino = tk.Radiobutton(text="Masculino", value=1, variable=var, command=escolha_feita)
masculino.grid(row=1, column=0)
feminino = tk.Radiobutton(text="Feminino", value=2, variable=var, command=escolha_feita)
feminino.grid(row=1, column=1)

cadeados_tamanho = (15, 15)
travar_nome_var = None
travar_sobrenome_var = None

cadeado_nome = Image.open("lock_nome.png")
cadeado_nome_img = cadeado_nome.resize(cadeados_tamanho)
cadeado_nome_ativo = Image.open("lock_nome_ativo.png")
cadeado_nome_ativo_img = cadeado_nome_ativo.resize(cadeados_tamanho)

cadeado_sobrenome = Image.open("lock_sobrenome.png")
cadeado_sobrenome_img = cadeado_sobrenome.resize(cadeados_tamanho)
cadeado_sobrenome_ativo = Image.open("lock_sobrenome_ativo.png")
cadeado_sobrenome_ativo_img = cadeado_sobrenome_ativo.resize(cadeados_tamanho)

cadeado_nome_icone = ImageTk.PhotoImage(image=cadeado_nome_img)
cadeado_sobrenome_icone = ImageTk.PhotoImage(image=cadeado_sobrenome_img)
cadeado_nome_ativo_icone = ImageTk.PhotoImage(image=cadeado_nome_ativo_img)
cadeado_sobrenome_ativo_icone = ImageTk.PhotoImage(image=cadeado_sobrenome_ativo_img)

cadeado_nome_btn = tk.Button(image=cadeado_nome_icone, highlightthickness=0, height=15, width=15,
                             command=travar_nome)  # CORRECT
cadeado_nome_btn.place(x=360, y=2)

cadeado_sobrenome_btn = tk.Button(image=cadeado_sobrenome_icone, highlightthickness=0, height=15, width=15,
                                  command=travar_sobrenome)  # CORRECT
cadeado_sobrenome_btn.place(x=400, y=2)

retorno_nome = Image.open("return.png")
retorno_img = retorno_nome.resize(cadeados_tamanho)
retorno_icone = ImageTk.PhotoImage(image=retorno_img)

retorno_btn = tk.Button(image=retorno_icone, highlightthickness=0, height=15, width=15, command=exibir_nome_anterior)
retorno_btn.place(x=-14, y=42)

atual_nome = Image.open("current.png")
atual_img = atual_nome.resize(cadeados_tamanho)
atual_icone = ImageTk.PhotoImage(image=atual_img)

atual_btn = tk.Button(image=atual_icone, highlightthickness=0, height=15, width=15, command=exibir_nome_atual)
atual_btn.place(x=8, y=42)

gerar_btn = tk.Button(text="Gerar Nome", font=FONT, command=gerar_nome, background="light sea green")
gerar_btn.grid(row=2, column=0)

nome_gerado_lbl = tk.Label(text="", font=FONT)
nome_gerado_lbl.grid(row=2, column=1)

remover_btn = tk.Button(text="Remover Nome/Sobrenome", font=FONT, command=remover_nome, background="salmon")
remover_btn.grid(row=2, column=2, pady=10)

adicionar_entry = tk.Entry(width=15)
adicionar_entry.grid(row=3, column=0)

adicionar_nome_btn = tk.Button(text="Adicionar Nome", font=FONT, command=adicionar_nome, background="lime green")
adicionar_nome_btn.grid(row=3, column=1)

adicionar_sobrenome_btn = tk.Button(text="Adicionar Sobrenome", font=FONT, command=adicionar_sobrenome, background="lime green")
adicionar_sobrenome_btn.grid(row=3, column=2, pady=5)

sep = ttk.Separator(root, orient="horizontal")
sep.grid(row=4, column=0, columnspan=4, ipadx=300, pady=10)

abrir_nomes_mas_btn = tk.Button(text="Abrir nomes_mas.txt", font=FONT, command=abrir_nomes_mas_txt, background="light gray")
abrir_nomes_mas_btn.grid(row=5, column=0, pady=5)

abrir_nomes_fem_btn = tk.Button(text="Abrir nomes_fem.txt", font=FONT, command=abrir_nomes_fem_txt, background="light gray")
abrir_nomes_fem_btn.grid(row=5, column=1, pady=5)

abrir_sobrenomes_btn = tk.Button(text="Abrir sobrenomes.txt", font=FONT, command=abrir_sobrenomes_txt, background="light gray")
abrir_sobrenomes_btn.grid(row=5, column=2, pady=5)

root.mainloop()
