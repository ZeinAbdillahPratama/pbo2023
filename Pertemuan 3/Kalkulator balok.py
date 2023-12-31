import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    Panjang = float(txtPanjang.get())
    lebar = float(txtlebar.get())

    luas = Panjang * lebar

    txtLuas.delete(0, END)
    txtLuas.insert(END,luas)

def hitung_volume():
    Panjang = float(txtPanjang.get())
    lebar = float(txtlebar.get())
    Tinggi = float(txtTinggi.get())

    Volume = Panjang * lebar * Tinggi

    txtVolume.delete(0,END)
    txtVolume.insert(END, Volume)

def hitung():
    hitung_luas()
    hitung_volume()

app = tk.Tk()

app.title ("Kalkulator Mencari Luas dan Volume Balok")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

nametag = tk.Frame(frame, bg="yellow", height=30)
nametag.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

nama = Label(nametag, text="Zein Abdillah Pratama (220511020)", bg='yellow') 
nama.grid(row=6, column=0, sticky=W, padx=5, pady=5)

kelas = Label(nametag, text="R5 TIF 22 E", bg='yellow' ) 
kelas.grid(row=6, column=1, sticky='e', padx=5, pady=5)

#panjang
Panjang = Label (frame, text="Panjang:")
Panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#lebar
lebar = Label (frame, text="lebar:")
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#tinggi
Tinggi = Label (frame, text="Tinggi:")
Tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#textbox panjang
txtPanjang = Entry(frame)
txtPanjang.grid(row=0, column=1)

#Textbox Lebar
txtlebar = Entry(frame)
txtlebar.grid(row=1, column=1)

#textbox tinggi
txtTinggi = Entry(frame)
txtTinggi.grid(row=2,column=1 )

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)


volume = Label (frame, text="volume: ")
volume.grid(row=5, column=0, stick=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtVolume = Entry (frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()