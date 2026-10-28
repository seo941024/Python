class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, pos, e):
        new_node = Node(e)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            for _ in range(pos - 1):
                if cur is None:
                    raise IndexError("위치가 범위를 벗어났습니다.")
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
        self.size += 1

    def delete(self, pos):

        if self.is_empty():
            raise IndexError("리스트가 비어 있습니다.")
        if pos == 0:
            data = self.head.data
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(pos - 1):
                if cur.next is None:
                    raise IndexError("위치가 범위를 벗어났습니다.")
                cur = cur.next
            data = cur.next.data
            cur.next = cur.next.next
        self.size -= 1
        return data

    def is_empty(self): return self.size == 0

    def is_full(self): return False

    def get_entry(self, pos):
        cur = self.head
        for _ in range(pos):
            if cur is None:
                raise IndexError("위치가 범위를 벗어났습니다.")
            cur = cur.next
        if cur is None:
            raise IndexError("위치가 범위를 벗어났습니다.")
        return cur.data

    def size_of(self): return self.size

    def clear(self):
        self.head = None
        self.size = 0

    def find(self, item):
        cur = self.head
        idx = 0
        while cur:
            if cur.data == item:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def replace(self, pos, item):
        cur = self.head
        for _ in range(pos):
            if cur is None:
                raise IndexError("위치가 범위를 벗어났습니다.")
            cur = cur.next
        if cur is None:
            raise IndexError("위치가 범위를 벗어났습니다.")
        cur.data = item

    def sort(self, reverse=False):
        if self.size < 2:
            return
        for _ in range(self.size - 1):
            cur = self.head
            while cur.next:
                a, b = cur.data, cur.next.data
                if (a > b) != reverse:
                    cur.data, cur.next.data = b, a
                cur = cur.next

    def merge(self, other):
        cur = other.head
        while cur:
            self.append(cur.data)
            cur = cur.next

    def display(self):
        elements = []
        cur = self.head
        while cur:
            elements.append(str(cur.data))
            cur = cur.next
        print("HEAD -> " + " -> ".join(elements) + " -> None")

    def append(self, e):
        new_node = Node(e)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self.size += 1


# ── 테스트 ──────────────────────────────────────────
if __name__ == "__main__":
    ll = LinkedList()

    print("=== Append A, B, C, D, F ===")
    for ch in ["A", "C", "D", "F"]:
        ll.append(ch)
    ll.display()

    print("\n=== Insert B at pos 1, G at pos 2 ===")
    ll.insert(1, "B")
    ll.insert(2, "G")
    ll.display()

    print("\n=== Delete pos 2 ===")
    removed = ll.delete(2)
    print(f"삭제된 값: {removed}")
    ll.display()

    print("\n=== getEntry(1) ===")
    print(f"pos 1 의 값: {ll.get_entry(1)}")

    print("\n=== Find('D') ===")
    print(f"'D' 의 인덱스: {ll.find('D')}")

    print("\n=== Replace pos 0 → 'Z' ===")
    ll.replace(0, "Z")
    ll.display()

    print("\n=== Sort ===")
    ll.sort()
    ll.display()

    print("\n=== Merge with [X, Y] ===")
    other = LinkedList()
    other.append("X")
    other.append("Y")
    ll.merge(other)
    ll.display()

    print(f"\nSize: {ll.size_of()}")
    print(f"isEmpty: {ll.is_empty()}")
    print(f"isFull: {ll.is_full()}")

    print("\n=== Clear ===")
    ll.clear()
    ll.display()
    print(f"isEmpty after clear: {ll.is_empty()}")