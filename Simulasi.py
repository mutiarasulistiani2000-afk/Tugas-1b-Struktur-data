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

