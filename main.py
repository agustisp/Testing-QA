import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Tidak dapat membagi oleh nol"
    else:
        return a / b

def main():
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = int(input("Masukkan pilihan Anda: "))

    if pilihan == 1:
        print("Hasil: ", add(a, b))
    elif pilihan == 2:
        print("Hasil: ", subtract(a, b))
    elif pilihan == 3:
        print("Hasil: ", multiply(a, b))
    elif pilihan == 4:
        print("Hasil: ", divide(a, b))
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
