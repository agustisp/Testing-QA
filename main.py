import math
import unittest

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

class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(3.5, 2.5), 6.0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(2.5, 1.5), 1.0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 3), 0)
        self.assertEqual(multiply(4, 0), 0)
        self.assertEqual(multiply(2.5, 1.5), 3.75)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2.0)
        self.assertEqual(divide(0, 3), 0.0)
        self.assertEqual(divide(1, 0), "Tidak dapat membagi oleh nol")
        self.assertEqual(divide(2.5, 1.25), 2.0)

if __name__ == '__main__':
    unittest.main()
