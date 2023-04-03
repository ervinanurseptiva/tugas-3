class Mahasiswa:
    def __init__(self, nama, nim, prodi, nilai):
        self.__nama = nama
        self.__nim = nim
        self.__prodi = prodi
        self.__nilai= nilai
        
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama

    def get_nim(self):
        return self.__nim
    
    def set_nim(self, nim):
        self.__nim = nim

    def get_prodi(self):
        return self.__prodi
    
    def set_prodi(self, prodi):
        self.__prodi = prodi
        
    def get_nilai(self):
        return self.__nilai
    
    def set_nilai(self, nilai):
        self.__nilai = nilai

    
Mahasiswa_1 = Mahasiswa("Ervina NS", "24673008" , "PTI", 90)
print("================Menampilkan Data=================")
print('nama:',Mahasiswa_1.get_nama())
print('nim:',Mahasiswa_1.get_nim())
print('prodi:',Mahasiswa_1.get_prodi())
print('nilai:',Mahasiswa_1.get_nilai())

Mahasiswa_1.set_nama("Ervina Ns")
Mahasiswa_1.set_nim("24673008 ")
Mahasiswa_1.set_prodi("Teknik Sipil")
Mahasiswa_1.set_nilai(95)

print("===============Data Setelah Diubah=================")
print('nama:',Mahasiswa_1.get_nama())
print('nim:',Mahasiswa_1.get_nim())
print('prodi:',Mahasiswa_1.get_prodi())
print('nilai:',Mahasiswa_1.get_nilai())
