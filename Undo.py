
from antrean import Antrean
from undo import Undo

#  NOMOR 8 (FITUR ANTREAN)
# ==========================================================
print("=== SIMULASI FITUR ANTREAN ===")
queue = Antrean()

# 1. Operasi Penambahan data (Enqueue) 5 Mahasiswa
print("--- Langkah 1: Penambahan Data (Enqueue) ---")
queue.enqueue("01 - Mutiara")
queue.enqueue("02 - Ahya")
queue.enqueue("03 - Melisa")
queue.enqueue("04 - Nabila")
queue.enqueue("05 - Rahilya")
print("Kondisi Antrean:", queue.data, "\n")

# 2. Operasi Penghapusan data (Dequeue)
print("--- Langkah 2: Penghapusan Data (Dequeue) ---")
mahasiswa_keluar = queue.dequeue()
print(f"Mahasiswa yang dilayani: {mahasiswa_keluar}")
print("Kondisi Antrean saat ini:", queue.data, "\n")

# 3. Operasi Melihat data terdepan (Peek)
print("--- Langkah 3: Melihat Data Terdepan (Peek) ---")
mahasiswa_depan = queue.peek()
print(f"Mahasiswa di posisi paling depan: {mahasiswa_depan}")
print("Kondisi Antrean saat ini:", queue.data, "\n")

# 4. Operasi Memeriksa kondisi kosong (isEmpty)
print("--- Langkah 4: Memeriksa Kondisi Kosong (isEmpty) ---")
status_kosong = queue.is_empty()
print(f"Apakah antrean kosong? {status_kosong}")
print("Kondisi Antrean saat ini:", queue.data, "\n")


# ==========================================================
#  NOMOR 10 (FITUR UNDO)
print("\n=== SIMULASI FITUR UNDO ===")
undo_stack = Undo()

# Langkah 1: Push
print("--- Langkah 1: Push ---")
undo_stack.push("Menambahkan Antrean mahasiswa Mutiara")
print(f"Kondisi Struktur Data: {undo_stack.data}\n")

# Langkah 2: Push
print("--- Langkah 2: Push ---")
undo_stack.push("Menambahkan antrean mahasiswa Ahya")
print(f"Kondisi Struktur Data: {undo_stack.data}\n")

# Langkah 3: Push
print("--- Langkah 3: Push ---")
undo_stack.push("Mengubah Data mahasiswa Mutiara")
print(f"Kondisi Struktur Data: {undo_stack.data}\n")

# Langkah 4: Pop/Undo
print("--- Langkah 4: Pop/Undo ---")
aktivitas_dibatalkan = undo_stack.pop()
print(f"Aktivitas yang dibatalkan: '{aktivitas_dibatalkan}'")
print(f"Kondisi Struktur Data: {undo_stack.data}\n")

# Langkah 5: Peek
print("--- Langkah 5: Peek ---")
aktivitas_terakhir = undo_stack.peek()
print(f"Melihat aktivitas terakhir: '{aktivitas_terakhir}'")
print(f"Kondisi Struktur Data: {undo_stack.data}\n")