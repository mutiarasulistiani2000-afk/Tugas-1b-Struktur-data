import unittest

class Antrean:
    def __init__(self):
        self.data = []

    # Menambahkan mahasiswa ke belakang antrean
    def enqueue(self, mahasiswa):
        self.data.append(mahasiswa)

    # Mengambil mahasiswa paling depan
    def dequeue(self):
        if self.is_empty():
            return None
        return self.data.pop(0)

    # Melihat mahasiswa paling depan
    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]

    # Mengecek apakah antrean kosong
    def is_empty(self):
        return len(self.data) == 0
