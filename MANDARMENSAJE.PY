from ast import Break, Is, keyword
from asyncore import read
from ctypes.wintypes import PINT
from lib2to3.pgen2 import driver
from msilib.schema import ListBox
from multiprocessing.pool import CLOSE
from pickle import TRUE
from re import A, I, S, X
from unicodedata import name
from cv2 import dft

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import Image, Listbox, Tk, filedialog, ttk, messagebox
import tkinter as tk
import sys
import pyautogui
import time
import webbrowser
import pandas as pd

from datetime import datetime


def numeros_cargar ():
 archivo_abierto=filedialog.askopenfilename(initialdir="/",title="selecione archivo",
 filetypes=(("jpeg files","*.cvs"),("all files","*.*")))
 if archivo_abierto != "Error":
    df = pd.read_csv(archivo_abierto,delim_whitespace=False)
    lista_cargada.insert(tk.END ,df[0:-1])

    

def enviar_lista_cargada ():
  lista_cargada.get
  print(lista_cargada)

  
  

def enviar():
    pyautogui.move(300 , 400)
    
    cargar = entrada.get()
    if cargar != "Error":
        keyword = cargar
        webbrowser.open("https://web.whatsapp.com/send?phone=+549"+keyword)
        time.sleep(18)
        pyautogui.typewrite(texto.get("1.0", "end-1c")) 
        pyautogui.press('enter')

    
    if cargar != "Error":
     date = datetime.now()
     resultado = cargar
     lista_de_resultados.insert(tk.END, resultado)
     lista_de_resultados.insert(tk.END, date)
 
    
     





          	
def limpiar():
    entrada.delete(0,tk.END)
    texto.delete("1.0", "end-1c")
    
def salir():
    resultado = messagebox.askyesno(title="Pregunta",message="¿Desea salir?") 
    if resultado: 
        sys.exit()

def ayuda():
    messagebox.showwarning(title="Advertencia", message="Buena suerte..")

def autor():
    messagebox.showinfo(title="Información", message="Autor: FreeeVooo")


ventana_principal = tk.Tk()
ventana_principal.title("enviar mensaje")

# Menu de navegación
barra_de_menu = tk.Menu()

# SUB MENU
menu_archivo = tk.Menu(barra_de_menu, tearoff=0)
menu_ayuda = tk.Menu(barra_de_menu, tearoff=0)

barra_de_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_de_menu.add_cascade(label="Referencias", menu=menu_ayuda)

menu_archivo.add_command(label="Limpiar", command=limpiar)
menu_archivo.add_command(label="Salir", command=salir)

menu_ayuda.add_command(label="Ayuda", command=ayuda)
menu_ayuda.add_command(label="Autor", command=autor)

# Boton
boton_enviar = tk.Button(text="ENVIAR", command=enviar)
boton_enviar.place(x=400, y=320)
boton_cargar = tk.Button(text="CARGAR", command=numeros_cargar)
boton_cargar.place(x=250, y=50)
boton_enviar = tk.Button(text="BORRAR", command=limpiar)
boton_enviar.place(x=300, y=320)
boton_enviar_lista_cargada = tk.Button(text="ENVIAR LISTA CARGADA", command=enviar_lista_cargada)
boton_enviar_lista_cargada.place(x=100, y=320)

# ETIQUETAS
mensaje = ttk.Label(text="MENSAJE")
mensaje.place(x=300, y=80)
etiqueta_acumulados = ttk.Label(text="NUMEROS MANDADOS")
etiqueta_acumulados.place(x=20, y=110)


# LISTAS
lista_de_resultados = tk.Listbox()
lista_de_resultados.place(height=170, width=180 ,x=10, y=140)
lista_cargada = tk.Text()
lista_cargada.place(height=170, width=150 ,x=435, y=140)


# Entradas
entrada = tk.Entry()
entrada.place(x=100, y=50)
texto = tk.Text()
texto.place(height=200, width=250 ,x=180, y=110)
carga = tk.Entry()
carga.place(x=100, y=80)

ventana_principal.config(width=600, height=400, menu=barra_de_menu)
ventana_principal.mainloop()

