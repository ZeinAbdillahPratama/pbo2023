from db import DBConnection as mydb
class Kembalikankomik:
    def __init__(self):
        self.__Id=None
        self.__Nama_Konsumen=None
        self.__Judul_Komik=None
        self.__Jumlah_Komik=None
        self.__Tanggal_Dikembalikan=None
        self.__Tarif_PerHari=None
        self.__Total_Bayar=None
        self.__Status_Bayar=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def Id(self):
        return self.__Id
    @property
    def Nama_Konsumen(self):
        return self.__Nama_Konsumen
        
    @Nama_Konsumen.setter
    def Nama_Konsumen(self, value):
        self.__Nama_Konsumen = value
    @property
    def Judul_Komik(self):
        return self.__Judul_Komik
        
    @Judul_Komik.setter
    def Judul_Komik(self, value):
        self.__Judul_Komik = value
    @property
    def Jumlah_Komik(self):
        return self.__Jumlah_Komik
        
    @Jumlah_Komik.setter
    def Jumlah_Komik(self, value):
        self.__Jumlah_Komik = value
    @property
    def Tanggal_Dikembalikan(self):
        return self.__Tanggal_Dikembalikan
        
    @Tanggal_Dikembalikan.setter
    def Tanggal_Dikembalikan(self, value):
        self.__Tanggal_Dikembalikan = value
    @property
    def Tarif_PerHari(self):
        return self.__Tarif_PerHari
        
    @Tarif_PerHari.setter
    def Tarif_PerHari(self, value):
        self.__Tarif_PerHari = value
    @property
    def Total_Bayar(self):
        return self.__Total_Bayar
        
    @Total_Bayar.setter
    def Total_Bayar(self, value):
        self.__Total_Bayar = value
    @property
    def Status_Bayar(self):
        return self.__Status_Bayar
        
    @Status_Bayar.setter
    def Status_Bayar(self, value):
        self.__Status_Bayar = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__Nama_Konsumen,self.__Judul_Komik,self.__Jumlah_Komik,self.__Tanggal_Dikembalikan,self.__Tarif_PerHari,self.__Total_Bayar,self.__Status_Bayar)
        sql="INSERT INTO Kembalikankomik (Nama_Konsumen,Judul_Komik,Jumlah_Komik,Tanggal_Dikembalikan,Tarif_PerHari,Total_Bayar,Status_Bayar) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__Nama_Konsumen,self.__Judul_Komik,self.__Jumlah_Komik,self.__Tanggal_Dikembalikan,self.__Tarif_PerHari,self.__Total_Bayar,self.__Status_Bayar, id)
        sql="UPDATE kembalikankomik SET Nama_Konsumen = %s,Judul_Komik = %s,Jumlah_Komik = %s,Tanggal_Dikembalikan = %s,Tarif_PerHari = %s,Total_Bayar = %s,Status_Bayar = %s WHERE Id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMA_KONSUMEN(self, Nama_Konsumen):
        self.conn = mydb()
        val = (self.__Judul_Komik,self.__Jumlah_Komik,self.__Tanggal_Dikembalikan,self.__Tarif_PerHari,self.__Total_Bayar,self.__Status_Bayar, Nama_Konsumen)
        sql="UPDATE kembalikankomik SET Judul_Komik = %s,Jumlah_Komik = %s,Tanggal_Dikembalikan = %s,Tarif_PerHari = %s,Total_Bayar = %s,Status_Bayar = %s WHERE Nama_Konsumen=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM kembalikankomik WHERE Id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMA_KONSUMEN(self, Nama_Konsumen):
        self.conn = mydb()
        sql="DELETE FROM kembalikankomik WHERE Nama_Konsumen='" + str(Nama_Konsumen) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM kembalikankomik WHERE Id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__Id = self.result[0]
        self.__Nama_Konsumen = self.result[1]
        self.__Judul_Komik = self.result[2]
        self.__Jumlah_Komik = self.result[3]
        self.__Tanggal_Dikembalikan = self.result[4]
        self.__Tarif_PerHari = self.result[5]
        self.__Total_Bayar = self.result[6]
        self.__Status_Bayar = self.result[7]
        self.conn.disconnect
        return self.result
    def getByNAMA_KONSUMEN(self, Nama_Konsumen):
        a=str(Nama_Konsumen)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM kembalikankomik WHERE Nama_Konsumen='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__Id = self.result[0]
           self.__Nama_Konsumen = self.result[1]
           self.__Judul_Komik = self.result[2]
           self.__Jumlah_Komik = self.result[3]
           self.__Tanggal_Dikembalikan = self.result[4]
           self.__Tarif_PerHari = self.result[5]
           self.__Total_Bayar = self.result[6]
           self.__Status_Bayar = self.result[7]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__Id = ''
           self.__Nama_Konsumen = ''
           self.__Judul_Komik = ''
           self.__Jumlah_Komik = ''
           self.__Tanggal_Dikembalikan = ''
           self.__Tarif_PerHari = ''
           self.__Total_Bayar = ''
           self.__Status_Bayar = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM kembalikankomik"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,Judul_Komik FROM kembalikankomik"
        self.result = self.conn.findAll(sql)
        return self.result     