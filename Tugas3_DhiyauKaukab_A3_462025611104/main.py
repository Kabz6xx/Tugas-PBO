class Karyawan:
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

    def tampilkan_data(self):
        print("Nama     :", self.nama)
        print("Jabatan  :", self.jabatan)
        print("Gaji     :", self.gaji)

    def bonus_tahunan(self):
        bonus = self.gaji * 0.1
        print("Bonus Tahunan :", bonus)

    @staticmethod
    def perusahaan():
        print("Perusahaan : PT Maju Mundur")


karyawan1 = Karyawan("Andi", "Manager", 7000000)
karyawan2 = Karyawan("Budi", "Staff", 4000000)


print("=== Karyawan 1 ===")
karyawan1.tampilkan_data()
karyawan1.bonus_tahunan()

print()

print("=== Karyawan 2 ===")
karyawan2.tampilkan_data()
karyawan2.bonus_tahunan()

print()

Karyawan.perusahaan()

karyawan1.perusahaan()