class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            if (ops >= '0' and ops <= '9') or (ops >= '-0' and ops <= '-9'):
                stack.append(ops)
                print(stack)
            elif ops == '+':
                total = int(stack[-1]) + int(stack[-2])
                stack.append(str(total))
                print(stack)
            elif ops == 'C':
                stack.pop()
                print(stack)
            elif ops == 'D':
                stack.append(str(int(stack[-1])*2))
                print(stack)
        res = 0
        for i in stack:
            res += int(i)
        return res
            