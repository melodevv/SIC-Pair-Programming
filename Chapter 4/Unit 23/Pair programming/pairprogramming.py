class Dequeue:
    def __init__(self):
        self.queue = []
        self.sequence = []
        self.sequence2 = []

    def add_first(self, item):
        self.queue.append(item)

    def remove_first(self):
        self.sequence = self.queue.pop(0)
        return self.sequence

    def add_last(self, item):
        self.queue.insert(-1,item)

    def remove_last(self):
        self.sequence2 = self.queue.remove(0)
        return self.sequence2


deque = Dequeue()
deque.add_first("Siyabonga")
deque.add_first("Mpilonhle")
deque.add_first("Thato")
deque.add_last("Dimpho")

print(deque.remove_first())
print(deque.remove_first())
print(deque.remove_first())
print(deque.remove_first())
print(deque.remove_first())
print(deque.remove_last())
