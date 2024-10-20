# PROBLEM DESCRIPTON: https://leetcode.com/problems/richest-customer-wealth/description/
# SOLUTION SUMBITION WITH NUMPY: https://leetcode.com/problems/richest-customer-wealth/submissions/1428397229/
# SOLUTION WITH PURE PYTHON: https://leetcode.com/problems/richest-customer-wealth/submissions/1428399266/
# SOLUTION WITHOUT ANY FUNCTIONS: https://leetcode.com/problems/richest-customer-wealth/submissions/1428404078/
from typing import List
import numpy as np 

# SOLUTION WITH NUMPY - TOP 0.61%
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        accounts_wealth_per_customer = np.sum(accounts, axis=1)
        accounts_max_wealth  = np.max(accounts_wealth_per_customer)
        return int(accounts_max_wealth)

# # SOLUTION WITH PURE PYTHON - TOP 0.61%
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         accounts_wealth_per_customer = [sum(account) for account in accounts]
#         accounts_max_wealth = max(accounts_wealth_per_customer)
#         return accounts_max_wealth
    
# # SOLUTION WITHOUT ANY FUNCTIONS - TOP 0.61%
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         accounts_wealth_per_customer = []
#         for acc in accounts:
#             wealth = 0
#             for bank_money in acc:
#                 wealth += bank_money
#             accounts_wealth_per_customer.append(wealth)

#         max_wealth = accounts_wealth_per_customer[0]
#         for wealth in accounts_wealth_per_customer:
#             if wealth > max_wealth:
#                 max_wealth = wealth
        
#         return max_wealth

def test1():
    accounts = [[1,2,3],[3,2,1]]
    s = Solution()
    assert s.maximumWealth(accounts) == 6

def test2():
    accounts = [[1,5],[7,3],[3,5]]
    s = Solution()
    assert s.maximumWealth(accounts) == 10

def test3():
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    s = Solution()
    assert s.maximumWealth(accounts) == 17

if __name__=="__main__":
    test1()
    test2()
    test3()