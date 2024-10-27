# PROBLEM DESCRIPTON: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
# SOLUTION SUMBITION: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/submissions/1435236459/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num > 0:
            if num & 1 == 0:
                num >>= 1
            else:
                num -= 1
            counter += 1
        return counter

def tests():
    s = Solution()
    assert s.numberOfSteps(14) == 6
    assert s.numberOfSteps(8) == 4
    assert s.numberOfSteps(123) == 12
    assert s.numberOfSteps(0) == 0
    assert s.numberOfSteps(1) == 1

def main():
    tests()
    print("All tests passed.")

if __name__ == "__main__":
    main()