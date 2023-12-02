import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    rusuk = float(txtrusuk.get())

    L = 6 * rusuk ** 2

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    rusuk = float(txtrusuk.get())

    Volume = rusuk ** 3

    txtVolume.delete(0,END)
    txtVolume.insert(END,Volume)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Kubus")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

nametag = tk.Frame(frame, bg="yellow", height=30)
nametag.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

nama = Label(nametag, text="Zein Abdillah Pratama (220511020)", bg='yellow') 
nama.grid(row=6, column=0, sticky=W, padx=5, pady=5)

kelas = Label(nametag, text="R5 TIF 22 E", bg='yellow' ) 
kelas.grid(row=6, column=1, sticky='e', padx=5, pady=5)


# Label Rusuk
rusuk = Label(frame, text="Rusuk:") 
rusuk.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox Rusuk
txtrusuk = Entry(frame)
txtrusuk.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
Volume = Label (frame, text="Volume: ")
Volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry (frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()