# ============================================================
# 1. 고정 배열 기반 Queue (Circular Array Queue)
# ============================================================

class ArrayQueue:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, e):
        if self.is_full():
            print("overflow")
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = e
        return True

    def dequeue(self):
        if self.is_empty():
            print("underflow")
            return None
        self.front = (self.front + 1) % self.capacity
        item = self.queue[self.front]
        self.queue[self.front] = None
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[(self.front + 1) % self.capacity]

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def clear(self):
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0


# ============================================================
# 2. 연결 구조 기반 Queue (Linked Queue)
# ============================================================

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, e):
        node = Node(e)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self._size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("underflow")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def size(self):
        return self._size

    def clear(self):
        self.front = None
        self.rear = None
        self._size = 0


# ============================================================
# 테스트
# ============================================================

if __name__ == "__main__":
    print("=== ArrayQueue ===")
    aq = ArrayQueue()
    aq.enqueue('A'); aq.enqueue('B'); aq.enqueue('C')
    print(aq.peek())        # A
    print(aq.size())        # 3
    print(aq.dequeue())     # A
    print(aq.dequeue())     # B
    print(aq.size())        # 1