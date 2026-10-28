class Calculate:

    def check_brackets(self, expr):
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for ch in expr:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                if not stack or stack[-1] != match[ch]:
                    return "ERROR"
                stack.pop()

        return "OK" if not stack else "ERROR"

    def tokenize(self, expr):
        """공백 없이 붙여 쓴 식도 숫자·연산자·괄호 단위로 나눔"""
        tokens = []
        num = ''
        for ch in expr:
            if ch.isdigit() or ch == '.':
                num += ch
                continue
            # 식 맨 앞이나 연산자·여는 괄호 뒤의 -는 음수 부호
            prev = tokens[-1] if tokens else '('
            if ch == '-' and not num and prev in ('+', '-', '*', '/', '('):
                num = '-'
                continue
            if num:
                tokens.append(num)
                num = ''
            if not ch.isspace():
                tokens.append(ch)
        if num:
            tokens.append(num)
        return tokens

    def infix_to_postfix(self, expr):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        stack, result = [], []

        for token in self.tokenize(expr):
            if token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  # '(' 제거
            elif token in prec:
                while stack and stack[-1] != '(' and prec.get(stack[-1], 0) >= prec[token]:
                    result.append(stack.pop())
                stack.append(token)
            else:
                result.append(token)  # 숫자

        while stack:
            result.append(stack.pop())

        return ' '.join(result)

    def evaluate_postfix(self, expr):
        stack = []
        tokens = expr.split()

        for token in tokens:
            if token in ('+', '-', '*', '/'):
                # 연산자 앞에 숫자가 두 개 없으면 잘못된 식
                if len(stack) < 2:
                    raise ValueError("잘못된 수식입니다")
                b = stack.pop()
                a = stack.pop()
                if   token == '+': stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/':
                    q = a / b
                    stack.append(int(q) if q == int(q) else q)
            elif token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                try:
                    stack.append(float(token))
                except ValueError:
                    raise ValueError("잘못된 수식입니다")

        # 계산 후 숫자가 하나만 남아야 정상
        if len(stack) != 1:
            raise ValueError("잘못된 수식입니다")
        return stack[0]

    def evaluate_infix(self, expr):
        """중위식을 바로 계산 (두 메서드 연결)"""
        if self.check_brackets(expr) == "ERROR":
            raise ValueError("괄호 오류")
        postfix = self.infix_to_postfix(expr)
        return self.evaluate_postfix(postfix)


# 테스트
calc = Calculate()

print(calc.check_brackets("{ A[ (i+1) ]=0; }"))     # OK
print(calc.check_brackets("A( (i+1] )=0;"))          # ERROR

print(calc.infix_to_postfix("8 / 2 - 3 + 3 * 2"))   # 8 2 / 3 - 3 2 * +
print(calc.evaluate_postfix("8 2 / 3 - 3 2 * +"))   # 7
print(calc.evaluate_infix("8 / 2 - 3 + 3 * 2"))     # 7
print(calc.evaluate_infix("(1+2)*3"))               # 9
print(calc.evaluate_infix("7 / 2"))                 # 3.5

try:
    calc.evaluate_infix("1 2 + 3")
except ValueError as e:
    print("오류:", e)                                # 오류: 잘못된 수식입니다
