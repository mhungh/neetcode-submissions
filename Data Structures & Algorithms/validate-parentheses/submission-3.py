class Solution:
    def isValid(self, s: str) -> bool:
        d = "([{"
        st = []
        for i in s:
            if i in d:
                st.append(i)
            elif i == ')':
                if len(st) == 0 or st.pop() != '(':
                    return False
            elif i == ']':
                if len(st) == 0 or st.pop() != '[':
                    return False
            elif i == '}':
                if len(st) == 0 or st.pop() != '{':
                    return False
        
        return len(st) == 0