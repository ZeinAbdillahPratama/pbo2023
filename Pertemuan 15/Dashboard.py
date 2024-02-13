import tkinter as tk
from tkinter import ttk 
from FrmSewakomik import *
from FrmKembalikankomik import *

def new_window(_class):
	new = tk.Toplevel()
	new.transient()
	new.grab_set()
	_class(new)

# Window
window = tk.Tk()
window.title("Multiform")
window.geometry("300x200")

# Frame
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10)

nama = ttk.Label(frame, text="Zein Abdillah Pratama")
nama.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

nim = ttk.Label(frame, text="220511020")
nim.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

kelas = ttk.Label(frame, text="TIF22E")
kelas.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)

# Bar Menu
menu = tk.Menu(window)
window.config(menu=menu)

# Menu Calculator
menu.komik= tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Menu", menu=menu.komik)
menu.komik.add_command(label="sewakomik", command=lambda: new_window(FormSewakomik))
menu.komik.add_command(label="Kembalikankomik", command=lambda: new_window(FormKembalikankomik))


window.mainloop()