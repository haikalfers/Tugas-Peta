"""
    Kelompok 7_2023E - Tugas Graph Struktur Data

    1. Daniel Satria P.R.B - 23091397143 (Ketua)
    2. Ahmad Afredo F.A - 23091397150 (Reviewer)
    3. Alya Faadhilah P - 23091397153 (Notulis)
    4. Haikal Ferdian S - 23091397154 (Code Editor)
"""
# class node
class Peta:
    # metode inisiasi (init)
    def __init__(self):
        self.daftarKota = {}
        
    # metode tambahKota untuk menambahkan kota
    def tambahKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {}
    
    # metode printKota untuk menampilkan kota
    def printKota(self):
        for kota in self.daftarKota:
            print(f"{kota} -- {self.daftarKota[kota]}")
    
    # metode tambahJalan untuk menambahkan jarak antar kota
    def tambahJalan(self, kota1, kota2, jarak):
        # jika kota1 dan kota2 ada di daftarKota maka tambahkan jarak
        if kota1 and kota2 in self.daftarKota:
            self.daftarKota[kota1][kota2] = jarak
            self.daftarKota[kota2][kota1] = jarak

    # metode hapusKota untuk menghapus kota
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.daftarKota:
            for kota in self.daftarKota:
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            del self.daftarKota[kotaDihapus]
            
    # metode hapusJalan untuk menghapus jarak antar kota
    def hapusJalan(self, kota1, kota2):
        if kota1 and kota2 in self.daftarKota:
            del self.daftarKota[kota1][kota2]
            del self.daftarKota[kota2][kota1]

        # metode ruteTempuh untuk menampilkan jarak tempuh
    def ruteTempuh(self, kota1, kota2):
        # jika kota1 dan kota2 ada di daftarKota maka tampilkan jarak
        if kota1 and kota2 in self.daftarKota:
            # jika kota1 dan kota2 tidak ada di daftarKota maka tampilkan pesan
            if kota1 not in self.daftarKota [kota2] or kota2 not in self.daftarKota [kota1]:
                print("Kota harus melewati kota lain untuk sampai ke kota tujuan")
            else:
                print(self.daftarKota[kota1][kota2])
        
        # jika user menempuh antar kota yang tidak sesuai dengan daftarKota
        else:
            print("Kamu harus melewati kota lain untuk sampai ke kota tujuan")

# variabel untuk list nama kota di Filipina
PetaFilipina = ["General Santos", "Koronadal", "Digos", "Kidapawan", "Cotaboto", "Davao", "Samai", "Tagum", "Mati", "Valencia"]
# variabel untuk memanggil class Peta
Filipina = Peta()

# aturan untuk input nama kota
print("Masukkan nama kota sesuai dengan list dibawah ini:")
# menambahkan kota dalam class
for kota in PetaFilipina:
    Filipina.tambahKota(kota)
    
# menambahakn jarak antar kota yang dilalui
Filipina.tambahJalan("General Santos", "Koronadal", "Jarak: 58,5KM")
Filipina.tambahJalan("General Santos", "Digos", "Jarak: 88,5KM")
Filipina.tambahJalan("General Santos", "Kidapawan", "Jarak: 141KM")
Filipina.tambahJalan("General Santos", "Cotaboto", "Jarak: 186KM")
Filipina.tambahJalan("General Santos", "Davao", "Jarak: 142KM")
Filipina.tambahJalan("General Santos", "Samai", "Jarak: 161KM")
Filipina.tambahJalan("General Santos", "Tagum", "Jarak: 194KM")
Filipina.tambahJalan("General Santos", "Mati", "Jarak: 295KM")
Filipina.tambahJalan("Koronadal", "Digos", "Jarak: 89,2KM")
Filipina.tambahJalan("Digos", "Kidapawan", "Jarak: 52,8KM")
Filipina.tambahJalan("Kidapawan", "Cotaboto", "Jarak: 123KM")
Filipina.tambahJalan("Cotaboto", "Davao", "Jarak: 231KM")
Filipina.tambahJalan("Davao", "Samai", "Jarak: 19,3KM")
Filipina.tambahJalan("Samai", "Tagum", "Jarak: 53,9KM")
Filipina.tambahJalan("Tagum", "Mati", "Jarak: 111KM")
Filipina.tambahJalan("Mati", "Valencia", "Jarak: 274KM")

# memanggil metode printKota untuk menampilkan kota
Filipina.printKota()

# variabel untuk input nama kota
lokasiAwal = input("Masukkan nama kota asal: ")
# variabel untuk input nama kota tujuan
lokasiTujuan = input("Masukkan nama kota tujuan: ")
# menampilkan jarak tempuh
Filipina.ruteTempuh(lokasiAwal, lokasiTujuan)
