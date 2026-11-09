class Node :
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedSet:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def contain(self, e):
        current = self.head
        while current:
            if current.data == e:
                return True
            current = current.next
        return False
    
    def insert(self, e):
        if self.contain(e):
            print("이미 존재하는 item입니다.")
            return
        new_node = Node(e)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, e):
        if self.size == 0:
            print("set이 비어있습니다.")
            return
        
        prev = None
        current = self.head
        while current:
            if current.data == e:
                if prev is None:
                    self.head = current.next
                else :
                    prev.next = current.next
                self.size -= 1
                return e
            prev = current
            current = current.next
        
        print("존재하지 않는 item입니다.")

    # 연결 구조는 메모리가 허용하는 한 추가 가능
    def isfull(self): return False

    def isempty(self) : return True if self.size == 0 else False

    def union(self, setB):
        result = LinkedSet()
        for node in (self.head, setB.head):
            current = node
            while current:
                if not result.contain(current.data):
                    result.insert(current.data)
                current = current.next
        return result

    def intersect(self, setB):
        result = LinkedSet()
        current = self.head
        while current:
            if setB.contain(current.data):
                result.insert(current.data)
            current = current.next
        return result

    def difference(self, setB):
        result = LinkedSet()
        current = self.head
        while current:
            if not setB.contain(current.data):
                result.insert(current.data)
            current = current.next
        return result

    def equals(self, setB):
        if self.size != setB.size:
            return False
        return self.difference(setB).size == 0

    def check_size(self):
        return self.size

    def display(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        print(items)

'''• Contain(e): 집합이 원소 e를 포함하는지 검사한다
• Insert(e): 새로운 원소 e를 삽입한다. (중복 삽입은 허용안함)
• Delete(e): 원소 e를 집합에서 꺼내고(삭제) 반환한다
• IsFull(): 집합이 가득 차 있는지를 검사한다
• isEmpty(): 공집합인지 검사한다
• Union(setB): setB와 합집합을 만들어 반환한다
• intersect(setB): setB와 교집합을 만들어 반환한다
• Difference(setB): setB와 차집합을 만들어 반환한다
• Equals(setB): setB와 같은 집합인지를 검사한다
• Size(): 집합의 원소의 개수를 반환한다
• Display(): 리스트를 화면에 출력한다'''


a = LinkedSet()
b = LinkedSet()

a.insert(1); a.insert(2); a.insert(3)
b.insert(2); b.insert(3); b.insert(4)

print("=== display ===")
a.display()
b.display()

print("\n=== insert 중복 ===")
a.insert(2)

print("\n=== delete ===")
print(a.delete(1))
a.display()
a.delete(99)

print("\n=== union ===")
a.union(b).display()

print("\n=== intersect ===")
a.intersect(b).display()

print("\n=== difference ===")
a.difference(b).display()

print("\n=== equals ===")
print(a.equals(b))
print(a.equals(a))

print("\n=== check_size ===")
print(a.check_size())
