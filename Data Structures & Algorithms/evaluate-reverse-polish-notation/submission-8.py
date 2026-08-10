class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        
        for i in tokens:
            if i == '+':
                a = s.pop()
                b = s.pop()
                r = a+b
                s.append(r)
            elif i == '-':
                a = s.pop()
                b = s.pop()
                r = b-a
                s.append(r)
            elif i == '*':
                a = s.pop()
                b = s.pop()
                r = a*b
                s.append(r)
            elif i == '/':
                a = s.pop()
                b = s.pop()
                r = 0
                if a*b>0:
                    r = b//a
                elif a < 0:
                    r = (b)//(-a)
                    r = -r
                elif b < 0:
                    r = (-b)//(a)
                    r = -r
                    
                s.append(r)
            else:
                a = int(i)
                s.append(a)

        return s[0]