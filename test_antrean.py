import unittest

class Antrean:
    def __init__(self):
        self.data = []
    def enqueue(self, mahasiswa):
        self.data.append(mahasiswa)
    def dequeue(self):
        return None if self.is_empty() else self.data.pop(0)
    def peek(self):
        return None if self.is_empty() else self.data[0]
    def is_empty(self):
        return len(self.data) == 0

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Antrean()
        queue.enqueue("Mutiara")
        self.assertEqual(queue.data, ["Mutiara"])
        
    def test_dequeue(self):
        queue = Antrean()
        queue.enqueue("Mutiara")
        hasil = queue.dequeue()
        self.assertEqual(hasil, "Mutiara")
        self.assertTrue(queue.is_empty())
        
    def test_peek(self):
        queue = Antrean()
        queue.enqueue("Mutiara")
        queue.enqueue("Ahya")
        self.assertEqual(queue.peek(), "Mutiara")
        
    def test_is_empty(self):
        queue = Antrean()
        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main()