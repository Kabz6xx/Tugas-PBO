class Laptop:
    def __init__(self, merk, ram, processor, VGA):
        self.merk = merk
        self.ram = ram
        self.processor = processor
        self.VGA = VGA


# Membuat object
laptop1 = Laptop("ASUS TUF", "16GB", "Intel i7 12450H", "RTX 3050 4GB")
laptop2 = Laptop("Lenovo Legion", "32GB", "AMD Ryzen 9 9950X3D", "RTX 5090 12GB")


# Menampilkan object
print(f"Laptop 1 -> Merk: {laptop1.merk}, RAM: {laptop1.ram}, Processor: {laptop1.processor}, VGA: {laptop1.VGA}")
print(f"Laptop 2 -> Merk: {laptop2.merk}, RAM: {laptop2.ram}, Processor: {laptop2.processor}, VGA: {laptop2.VGA}")