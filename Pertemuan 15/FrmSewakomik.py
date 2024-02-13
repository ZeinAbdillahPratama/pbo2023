import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Sewakomik import Sewakomik
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry

class FormSewakomik:   
    def __init__(self, parent):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(Sewakomik)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='NAMA_KONSUMEN:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA_KONSUMEN
        self.txtNAMA_KONSUMEN = Entry(mainFrame) 
        self.txtNAMA_KONSUMEN.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNAMA_KONSUMEN.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # varchar 
        Label(mainFrame, text='JUDUL_KOMIK:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox JUDUL_KOMIK
        self.txtJUDUL_KOMIK = Entry(mainFrame) 
        self.txtJUDUL_KOMIK.grid(row=1, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='JUMLAH_KOMIK:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox JUMLAH_KOMIK
        self.txtJUMLAH_KOMIK = Entry(mainFrame) 
        self.txtJUMLAH_KOMIK.grid(row=2, column=1, padx=5, pady=5)
                
         # date 
        Label(mainFrame, text='TANGGAL_DISEWAKAN:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL_DISEWAKAN
        self.txtTANGGAL_DISEWAKAN = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL_DISEWAKAN.grid(row=3, column=1, padx=5, pady=5)
                    
         # int 
        Label(mainFrame, text='TARIF_PERHARI:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Textbox TARIF_PERHARI
        self.txtTARIF_PERHARI = Entry(mainFrame) 
        self.txtTARIF_PERHARI.grid(row=4, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='TOTAL_BAYAR:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Textbox TOTAL_BAYAR
        self.txtTOTAL_BAYAR = Entry(mainFrame) 
        self.txtTOTAL_BAYAR.grid(row=5, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='STATUS_BAYAR:').grid(row=6, column=0, sticky=W, padx=5, pady=5)
        # Textbox STATUS_BAYAR
        self.txtSTATUS_BAYAR = Entry(mainFrame) 
        self.txtSTATUS_BAYAR.grid(row=6, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('Id','Nama_Konsumen','Judul_Komik','Jumlah_Komik','Tanggal_Disewakan','Tarif_PerHari','Total_Bayar','Status_Bayar')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('Id', text='Id')
        self.tree.column('Id', width="30")
        self.tree.heading('Nama_Konsumen', text='Nama_Konsumen')
        self.tree.column('Nama_Konsumen', width="30")
        self.tree.heading('Judul_Komik', text='Judul_Komik')
        self.tree.column('Judul_Komik', width="100")
        self.tree.heading('Jumlah_Komik', text='Jumlah_Komik')
        self.tree.column('Jumlah_Komik', width="100")
        self.tree.heading('Tanggal_Disewakan', text='Tanggal_Disewakan')
        self.tree.column('Tanggal_Disewakan', width="100")
        self.tree.heading('Tarif_PerHari', text='Tarif_PerHari')
        self.tree.column('Tarif_PerHari', width="100")
        self.tree.heading('Total_Bayar', text='Total_Bayar')
        self.tree.column('Total_Bayar', width="100")
        self.tree.heading('Status_Bayar', text='Status_Bayar')
        self.tree.column('Status_Bayar', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA_KONSUMEN.delete(0,END)
        self.txtNAMA_KONSUMEN.insert(END,"")
                                
        self.txtJUDUL_KOMIK.delete(0,END)
        self.txtJUDUL_KOMIK.insert(END,"")
                                
        self.txtJUMLAH_KOMIK.delete(0,END)
        self.txtJUMLAH_KOMIK.insert(END,"")
                                
        self.txtTARIF_PERHARI.delete(0,END)
        self.txtTARIF_PERHARI.insert(END,"")
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,"")
                                
        self.txtSTATUS_BAYAR.delete(0,END)
        self.txtSTATUS_BAYAR.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data sewakomik
        obj = Sewakomik()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        Nama_Konsumen = self.txtNAMA_KONSUMEN.get()
        obj = Sewakomik()
        res = obj.getByNAMA_KONSUMEN(Nama_Konsumen)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        Nama_Konsumen = self.txtNAMA_KONSUMEN.get()
        obj = Sewakomik()
        res = obj.getByNAMA_KONSUMEN(Nama_Konsumen)
            
        self.txtJUDUL_KOMIK.delete(0,END)
        self.txtJUDUL_KOMIK.insert(END,obj.Judul_Komik)
                                
        self.txtJUMLAH_KOMIK.delete(0,END)
        self.txtJUMLAH_KOMIK.insert(END,obj.Jumlah_Komik)
                                
        self.txtTANGGAL_DISEWAKAN.delete(0,END)
        self.txtTANGGAL_DISEWAKAN.insert(END,obj.Tanggal_Disewakan)
                                
        self.txtTARIF_PERHARI.delete(0,END)
        self.txtTARIF_PERHARI.insert(END,obj.Tarif_PerHari)
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,obj.Total_Bayar)
                                
        self.txtSTATUS_BAYAR.delete(0,END)
        self.txtSTATUS_BAYAR.insert(END,obj.Status_Bayar)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        Nama_Konsumen = self.txtNAMA_KONSUMEN.get()
        Judul_Komik = self.txtJUDUL_KOMIK.get()
        Jumlah_Komik = self.txtJUMLAH_KOMIK.get()
        Tanggal_Disewakan = self.txtTANGGAL_DISEWAKAN.get()
        Tarif_PerHari = self.txtTARIF_PERHARI.get()
        Total_Bayar = self.txtTOTAL_BAYAR.get()
        Status_Bayar = self.txtSTATUS_BAYAR.get()       
        obj = Sewakomik()
        obj.Nama_Konsumen = Nama_Konsumen
        obj.Judul_Komik = Judul_Komik
        obj.Jumlah_Komik = Jumlah_Komik
        obj.Tanggal_Disewakan = Tanggal_Disewakan
        obj.Tarif_PerHari = Tarif_PerHari
        obj.Total_Bayar = Total_Bayar
        obj.Status_Bayar = Status_Bayar
        if(self.ditemukan==True):
            res = obj.updateByNAMA_KONSUMEN(Nama_Konsumen)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        Nama_Konsumen = self.txtNAMA_KONSUMEN.get()
        obj = Sewakomik()
        obj.Nama_Konsumen = Nama_Konsumen
        if(self.ditemukan==True):
            res = obj.deleteByNAMA_KONSUMEN(Nama_Konsumen)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormSewakomik(root)
    root.mainloop() 