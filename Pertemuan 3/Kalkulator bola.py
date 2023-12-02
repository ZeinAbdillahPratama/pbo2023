import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
import math

def hitung_luas():
    jari_jari= float(txtjari_jari.get())

    L = 4 * math.pi * jari_jari


    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    jari_jari = float(txtjari_jari.get())

    volume = (4/3) * math.pi * jari_jari

    txtvolume.delete(0,END)
    txtvolume.insert(END,volume)


def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Bola")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

nametag = tk.Frame(frame, bg="yellow", height=30)
nametag.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

nama = Label(nametag, text="Zein Abdillah Pratama (220511020)", bg='yellow') 
nama.grid(row=6, column=0, sticky=W, padx=5, pady=5)

kelas = Label(nametag, text="R5 TIF 22 E", bg='yellow' ) 
kelas.grid(row=6, column=1, sticky='e', padx=5, pady=5)

#Label Jari-Jari
jari_jari = Label(frame, text="Jari-jari:")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Textbox Jari-jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label volume
volume = Label(frame, text="volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

#output Textbox volume
txtvolume = Entry (frame)
txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()