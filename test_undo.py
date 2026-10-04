import unittest

class Undo:
    def __init__(self):
        self.data = []
    def push(self, aktivitas):
        self.data.append(aktivitas)
    def pop(self):
        return None if self.is_empty() else self.data.pop()
    def peek(self):
        return None if self.is_empty() else self.data[-1]
    def is_empty(self):
        return len(self.data) == 0

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Undo()
        stack.push("Menambahkan Antrean mahasiswa Mutiara")
        self.assertEqual(stack.data, ["Menambahkan Antrean mahasiswa Mutiara"])
        
    def test_pop(self):
        stack = Undo()
        stack.push("Menambahkan Antrean mahasiswa Mutiara")
        hasil = stack.pop()
        self.assertEqual(hasil, "Menambahkan Antrean mahasiswa Mutiara")
        self.assertTrue(stack.is_empty())
        
    def test_peek(self):
        stack = Undo()
        stack.push("Menambahkan Antrean mahasiswa Mutiara")
        self.assertEqual(stack.peek(), "Menambahkan Antrean mahasiswa Mutiara")
        
    def test_is_empty(self):
        stack = Undo()
        self.assertTrue(stack.is_empty())

if __name__ == '__main__':
    unittest.main()