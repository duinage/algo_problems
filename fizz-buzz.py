# PROBLEM DESCRIPTON: https://leetcode.com/problems/fizz-buzz/description/
# SOLUTION SUMBITION: https://leetcode.com/problems/fizz-buzz/submissions/1435218420/
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

def test1():
    n = 3
    s = Solution()
    assert s.fizzBuzz(n) == ["1","2","Fizz"]

def test2():
    n = 5
    s = Solution()
    assert s.fizzBuzz(n) == ["1","2","Fizz","4","Buzz"]

def test3():
    n = 15
    s = Solution()
    assert s.fizzBuzz(n) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

if __name__=="__main__":
    test1()
    test2()
    test3()