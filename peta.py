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
        self.jumlahKota = 0
        
    # metode menampilkan kota pada peta
    def printKota(self):
        for kota in self.daftarKota:
            print(f"{kota}")
            for kotaTetangga, jarak in self.daftarKota[kota].items():
                print(f"\t--> {jarak} km -- {kotaTetangga}")
                
        print(f"Jumlah Kota : {self.jumlahKota}\n")

    # metode tambahKota untuk menambahkan kota
    def tambahKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {}
            self.jumlahKota += 1
    
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

# menambahkan kota dalam class
for kota in PetaFilipina:
    Filipina.tambahKota(kota)
    
# menambahkan jarak antar kota yang dilalui
Filipina.tambahJalan("General Santos", "Koronadal", 58.5)
Filipina.tambahJalan("General Santos", "Digos", 88.5)
Filipina.tambahJalan("Koronadal", "Digos", 89.2)
Filipina.tambahJalan("Koronadal", "Kidapawan", 80)
Filipina.tambahJalan("Koronadal", "Cotabato", 110)
Filipina.tambahJalan("Digos", "Kidapawan", 52.8)
Filipina.tambahJalan("Digos", "Davao", 106)
Filipina.tambahJalan("Cotabato", "Davao", 231)
Filipina.tambahJalan("Davao", "Samal", 19.3)
Filipina.tambahJalan("Davao", "Kidapawan", 95)
Filipina.tambahJalan("Davao", "Valencia", 163)
Filipina.tambahJalan("Samal", "Tagum", 53.9)
Filipina.tambahJalan("Tagum", "Mati", 111)
Filipina.tambahJalan("Tagum", "Valencia", 274)

# aturan untuk input nama kota
print("Masukkan nama kota sesuai dengan list dibawah ini:")
# memanggil metode printKota untuk menampilkan kota
print("___PETA FILIPINA___\n")
Filipina.printKota()

#menghitung jarak kota asal ke kota tujuan
print("___Menghitung Jarak___")

# variabel untuk input nama kota
lokasiAwal = input("Masukkan nama kota asal: ")
# variabel untuk input nama kota tujuan
lokasiTujuan = input("Masukkan nama kota tujuan: ")

# menampilkan jarak tempuh
Filipina.ruteTempuh(lokasiAwal, lokasiTujuan)
# menjalankan algoritma dijkstra
Filipina.dijkstra(lokasiAwal, lokasiTujuan)
