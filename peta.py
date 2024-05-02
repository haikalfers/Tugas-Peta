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
# menambahkan kota dalam class
for kota in PetaFilipina:
    Filipina.tambahKota(kota)
