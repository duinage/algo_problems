# PROBLEM DESCRIPTON: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# SOLUTION SUMBITION: https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1420954531/
from typing import List


class Solution:
    OPERATORS = ['+', '-', '*', '/']

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in Solution.OPERATORS:
                # token is number
                stack.append(float(token))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                operation_result = Solution.operation(left_operand, token, right_operand)
                stack.append(operation_result)

        eval_result = int(stack.pop())
        return eval_result

    @staticmethod
    def operation(left_operand, operator, right_operand):
        assert operator in Solution.OPERATORS

        match operator:
            case '+':
                return left_operand + right_operand
            case '-':
                return left_operand - right_operand
            case '*':
                return left_operand * right_operand
            case '/':
                return Solution.divide_but_truncates_toward_zero(left_operand, right_operand)
    
    divide_but_truncates_toward_zero = lambda left, right: int(left / right)


def test1():
    tokens = ["2","1","+","3","*"]
    s = Solution()
    assert s.evalRPN(tokens) == 9

def test2():
    tokens = ["4","13","5","/","+"]
    s = Solution()
    assert s.evalRPN(tokens) == 6

def test3():
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    s = Solution()
    assert s.evalRPN(tokens) == 22

if __name__=="__main__":
    test1()
    test2()
    test3()