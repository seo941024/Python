class Set:
    def __init__(self):
        self.MAX_SIZE = 10
        self.data = [None] * self.MAX_SIZE
        self.size = 0

    def _print_error(self, code):
        messages = {
            "full"    : "원소가 가득 찼습니다.",
            "pos"     : "위치 값을 다시 입력해주세요.",
            "empty"   : "리스트의 item이 비어있습니다.",
            "same"    : "중복된 값은 넣을 수 없습니다.",
            "notin"   : "존재하지 않는 원소입니다."
        }
        if code in messages:
            print(messages[code])

    def insert(self, e):
        if self.size == self.MAX_SIZE:
            self._print_error("full")
            return 
        
        for i in range(self.size) :
            if self.data[i] == e:
                self._print_error("same")
                return
            
        self.data[self.size] = e
        self.size +=1

    def delete(self, e):
        if self.size == 0:
            self._print_error("empty")
            return
        for i in range(self.size):
            if self.data[i] == e:
                # 뒤 원소를 한 칸씩 당겨 빈칸 없애기
                for j in range(i, self.size - 1):
                    self.data[j] = self.data[j + 1]
                self.data[self.size - 1] = None
                self.size -= 1
                return e

        self._print_error("notin")
            
    def isfull(self): return True if self.size==self.MAX_SIZE else False

    def isempty(self): return True if self.size==0 else False

    def union(self, setB):
        result = Set()
        result.MAX_SIZE = self.MAX_SIZE + setB.MAX_SIZE  # 20으로 확장
        result.data = [None] * result.MAX_SIZE
        for i in self.data[:self.size]:
            result.insert(i)
        for j in setB.data[:setB.size]:
            result.insert(j)
        return result
    
    def intersect(self, setB):
        result = Set()
        if self.size < setB.size:
            result.MAX_SIZE = self.size
        else:
            result.MAX_SIZE = setB.size

        result.data = [None] * result.MAX_SIZE

        for i in self.data[:self.size]:
            for j in setB.data[:setB.size]:
                if i == j:
                    result.insert(i)
        return result
    
    def difference(self, setB):
        result = Set()
        result.MAX_SIZE = self.size
        result.data = [None] * result.MAX_SIZE

        for i in self.data[:self.size]:
            found = False
            for j in setB.data[:setB.size]:
                if i == j:
                    found = True
                    break
            if not found:
                result.insert(i)
        return result
    
    def equals(self, setB):
        if self.size != setB.size:
            return False
        diff = self.difference(setB)
        if diff.size == 0:
            return True
        else:
            return False
        
    def check_size(self):
        return self.size
    
    def display(self):
        print(self.data[:self.size])

a = Set()
b = Set()

a.insert(1); a.insert(2); a.insert(3)
b.insert(2); b.insert(3); b.insert(4)

# display
print("=== display ===")
a.display()
b.display()

# insert 중복
print("\n=== insert 중복 ===")
a.insert(2)

# delete
print("\n=== delete ===")
a.delete(1)
a.display()
a.delete(99)  # 없는 원소

# isfull / isempty
print("\n=== isfull / isempty ===")
print(a.isfull())
print(a.isempty())

# union
print("\n=== union ===")
c = a.union(b)
c.display()

# intersect
print("\n=== intersect ===")
d = a.intersect(b)
d.display()

# difference
print("\n=== difference ===")
e = a.difference(b)
e.display()

# equals
print("\n=== equals ===")
print(a.equals(b))
print(a.equals(a))

# check_size
print("\n=== check_size ===")
print(a.check_size())