class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }

        valid = []

        for l in s:
            if l == '{' or l == '[' or l == '(':
                valid.append(l)

            elif l == ']' or l == '}' or l == ")":
                if len(valid) == 0 or parenthesis[l] != valid.pop():
                    return False 

        if len(valid) == 0:
            return True

        return False