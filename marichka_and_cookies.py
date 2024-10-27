# PROBLEM DESCRIPTON: https://algotester.com/en/ArchiveProblem/DisplayWithEditor/2
# SOLUTION SUMBITION: https://algotester.com/en/ProblemSolution/Display/1845410

# class Solution:
#     def max_cookies_for_marichka(self, cookies_in_each_pack: list) -> int:
#         max_cookies_amount = 0
#         for cookies in cookies_in_each_pack:
#             max_cookies_amount += cookies - 1
#         return max_cookies_amount

# def tests():
#     line1 = "4" # input()
#     line2 = "4 7 47 74" # input()
#     line2_list = [int(num) for num in line2.split()]
#     s = Solution()
#     assert s.max_cookies_for_marichka(line2_list) == 128


# def main():
#     tests()
#     print("All tests passed.")

# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    _ = input()
    print(sum(int(num) - 1 for num in input().split()))