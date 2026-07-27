class DompetDigital:
    def __init__(self, nama, pin, saldo):
        # Private Attributes
        self.__nama = nama
        self.__pin = pin
        self.__saldo = saldo

    def get_nama(self):
        return self.__nama

    def cek_saldo(self, pin):
        if pin == self.__pin:
            print("Saldo anda : Rp", self.__saldo)
        else:
            print("PIN salah!")

    def tarik_uang(self, pin, jumlah):
        if pin == self.__pin:
            if jumlah <= self.__saldo:
                self.__saldo -= jumlah
                print("Tarik uang berhasil")
                print("Sisa saldo : Rp", self.__saldo)
            else:
                print("Saldo tidak cukup")
        else:
            print("PIN salah!")


akun1 = DompetDigital("Yanto", "1234", 500000)

print("Nama Pemilik :", akun1.get_nama())

print()

print("Cek saldo dengan PIN benar")
akun1.cek_saldo("1234")

print()

print("Cek saldo dengan PIN salah")
akun1.cek_saldo("0000")

print()

akun1.tarik_uang("1234", 100000)

print()

akun1.tarik_uang("1111", 50000)