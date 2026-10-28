# 선형 덱(Linear Deque) - 배열로 구현
# 선형 큐와 마찬가지로 front, rear가 한 방향으로만 이동합니다.
# 앞(front)과 뒤(rear) 양쪽에서 삽입/삭제가 모두 가능합니다.

class LinearDeque:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # 맨 앞 요소의 바로 앞 인덱스
        self.rear = -1   # 맨 뒤 요소의 인덱스

    def is_full(self):
        # rear가 배열 끝에 닿으면 가득 찬 것으로 판단
        return self.rear == self.capacity - 1

    def is_empty(self):
        return self.front == self.rear

    def add_rear(self, e):
        # 뒤(rear)에 요소를 추가합니다
        if self.is_full():
            print("overflow — 덱이 가득 찼습니다")
            return False
        self.rear += 1
        self.queue[self.rear] = e
        return True

    def add_front(self, e):
        # 앞(front)에 요소를 추가합니다
        # front가 -1이면 앞쪽 빈칸 없음, 음수 인덱스 기록 방지
        if self.front < 0:
            print("overflow — 앞쪽 공간이 없습니다")
            return False
        self.queue[self.front] = e
        self.front -= 1
        return True

    def delete_front(self):
        # 앞(front)에서 요소를 꺼냅니다
        if self.is_empty():
            print("underflow — 덱이 비어있습니다")
            return None
        self.front += 1
        item = self.queue[self.front]
        self.queue[self.front] = None
        return item

    def delete_rear(self):
        # 뒤(rear)에서 요소를 꺼냅니다
        if self.is_empty():
            print("underflow — 덱이 비어있습니다")
            return None
        item = self.queue[self.rear]
        self.queue[self.rear] = None
        self.rear -= 1
        return item

    def get_front(self):
        # 앞 요소를 삭제하지 않고 확인만 합니다
        if self.is_empty():
            return None
        return self.queue[self.front + 1]

    def get_rear(self):
        # 뒤 요소를 삭제하지 않고 확인만 합니다
        if self.is_empty():
            return None
        return self.queue[self.rear]

    def size(self):
        return self.rear - self.front

    def clear(self):
        for i in range(self.capacity):
            self.queue[i] = None
        self.front = -1
        self.rear = -1

    def print_deque(self):
        if self.is_empty():
            print("[]")
            return
        result = '['
        for i in range(self.front + 1, self.rear + 1):
            result += str(self.queue[i])
            if i != self.rear:
                result += ', '
        result += ']'
        print(result)


# 테스트
d = LinearDeque()

d.add_front('X')   # overflow — 앞쪽 공간이 없습니다

d.add_rear('A')
d.add_rear('B')
d.add_rear('C')
print(d.delete_front())    # A
d.add_front('A')   # 꺼낸 앞쪽 빈칸에 다시 추가

d.print_deque()            # [A, B, C]
print(d.get_front())       # A
print(d.get_rear())        # C
print(d.size())            # 3

print(d.delete_front())    # A
print(d.delete_rear())     # C
d.print_deque()            # [B]
