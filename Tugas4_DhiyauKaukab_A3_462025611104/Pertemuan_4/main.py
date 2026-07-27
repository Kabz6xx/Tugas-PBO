class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"Produk: {self.nama}, Harga: Rp{self.harga}"

    def __eq__(self, other):
        return self.harga == other.harga

    def __lt__(self, other):
        return self.harga < other.harga

    def __gt__(self, other):
        return self.harga > other.harga


produk1 = Produk("Laptop", 8000000)
produk2 = Produk("Mouse", 200000)
produk3 = Produk("Keyboard", 200000)


print(produk1)
print(produk2)
print(produk3)

print()

print("Apakah Laptop lebih mahal dari Mouse?")
print(produk1 > produk2)

print()

print("Apakah Mouse lebih murah dari Laptop?")
print(produk2 < produk1)

print()

print("Apakah Mouse dan Keyboard harganya sama?")
print(produk2 == produk3)