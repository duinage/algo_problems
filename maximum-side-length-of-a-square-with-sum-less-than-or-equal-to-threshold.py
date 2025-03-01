# PROBLEM DESCRIPTON: https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/
# SOLUTION SUMBITION: 
from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        res = 0
        r_len, c_len = len(mat), len(mat[0])
        max_sq_len = min(r_len, c_len)

        low, high = 1,  max_sq_len
        while low <= high:
            found = False
            sq_len = low + (high-low)//2

            initial_sq_sum = 0
            for i in range(sq_len):
                for j in range(sq_len):
                    initial_sq_sum += mat[i][j]

            if initial_sq_sum <= threshold:
                res = sq_len
                found = True
            else:
                prev_sum = initial_sq_sum
                sq_sum = prev_sum
                for r_add in range(0,r_len-sq_len):
                    
                    for c_add in range(0,c_len-sq_len):
                        sq_sum -= sum(mat[i+r_add][c_add] for i in range(sq_len))
                        sq_sum += sum(mat[i+r_add][sq_len+c_add] for i in range(sq_len))
                        if sq_sum <= threshold and res < sq_len:
                            res = sq_len
                            found = True
                    else:
                        sq_sum = prev_sum

                    sq_sum -= sum(mat[r_add][i] for i in range(sq_len))
                    sq_sum += sum(mat[sq_len+r_add][i] for i in range(sq_len))
                    prev_sum = sq_sum
                    if sq_sum <= threshold and res < sq_len:
                        res = sq_len
                        found = True
                else:
                    for c_add in range(0,c_len-sq_len):
                        sq_sum -= sum(mat[i+r_len-sq_len][c_add] for i in range(sq_len))
                        sq_sum += sum(mat[i+r_len-sq_len][sq_len+c_add] for i in range(sq_len))
                        if sq_sum <= threshold and res < sq_len:
                            res = sq_len
                            found = True
            
            if found:
                low = sq_len + 1
            else:
                high = sq_len - 1

        return res

def tests():
    s = Solution()
    assert 2 == s.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]],4)
    assert 0 == s.maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],1)
    assert 1 == s.maxSideLength([[0]],0) 
    assert 10 == s.maxSideLength([[93,76,38,49,22,87,0,65,94,96,18,82,97,58,39,29,90,33,23,95,61,88,89,16,73,15,84,51,37,57,64,54,50,77,42,6,5,35,8,1,100,45,67,24,31],[83,98,1,76,79,14,81,35,47,85,58,55,20,75,44,12,27,15,38,52,67,87,78,88,90,4,26,23,5,18,49,100,25,31,0,32,74,37,65,10,53,3,94,51,61],[21,2,70,35,34,9,24,33,69,96,78,51,19,3,58,23,65,97,90,55,30,81,87,27,77,49,45,36,95,63,40,39,75,10,83,29,98,57,79,25,41,85,89,4,67],[60,71,61,36,32,58,47,37,84,77,48,16,42,75,20,70,68,69,2,22,72,98,15,80,62,9,63,59,12,97,30,78,3,91,5,39,86,56,34,66,81,29,67,93,55],[37,77,9,18,74,54,55,48,68,1,33,73,44,30,51,88,90,85,95,35,99,50,80,66,56,42,15,83,87,82,67,20,25,93,94,60,14,28,81,65,31,16,97,21,100],[21,73,59,36,94,26,41,60,53,69,83,27,40,56,22,13,0,29,42,86,14,5,30,24,92,43,95,28,47,6,78,35,76,4,75,39,45,58,67,9,10,44,77,84,15],[10,27,50,33,20,94,60,95,19,78,35,43,65,88,2,28,92,45,91,9,3,4,84,86,34,81,82,89,46,100,73,98,36,62,42,18,16,69,21,90,11,12,1,70,49],[30,75,15,80,35,94,57,81,63,38,14,61,65,32,25,33,37,46,28,97,4,8,58,68,9,31,0,39,11,26,79,84,100,47,40,21,41,17,56,78,18,52,96,88,34],[48,91,15,14,62,37,69,64,83,70,96,60,16,61,63,77,50,34,80,71,95,8,20,87,33,5,89,66,21,54,17,11,36,74,38,35,68,97,56,2,73,65,85,6,52],[38,3,65,48,29,95,37,32,69,40,34,25,71,63,44,13,30,7,11,4,52,88,45,21,6,33,28,72,23,31,27,97,5,93,58,77,18,74,85,35,56,20,78,62,79],[41,34,72,51,100,94,20,93,21,16,57,2,37,56,88,4,38,5,70,22,10,23,95,35,71,40,27,58,48,99,28,79,61,44,19,36,54,97,83,39,3,62,15,24,7],[42,15,74,88,87,16,13,50,26,55,94,38,12,63,99,86,76,46,0,39,9,8,65,11,52,28,14,43,67,100,30,33,40,57,7,78,54,6,77,93,59,56,21,98,27],[5,100,70,0,14,13,3,30,53,31,69,91,79,66,64,59,26,82,77,27,15,61,57,51,47,6,45,83,73,63,34,39,44,87,43,8,85,99,80,48,71,1,96,55,11],[4,52,86,3,84,35,38,43,92,37,67,17,56,61,98,16,11,57,85,25,21,96,53,65,71,55,47,40,70,58,87,83,26,68,19,0,91,76,46,62,30,8,82,22,89],[8,78,87,68,71,74,29,17,16,28,7,95,26,48,56,92,90,91,52,24,57,63,14,19,84,30,6,50,49,34,93,12,13,60,4,99,97,2,80,44,20,94,1,9,89],[69,0,65,85,19,9,72,14,43,18,28,73,78,87,67,27,59,63,53,2,89,96,8,26,84,91,22,42,4,61,71,54,1,17,49,47,100,24,46,93,70,48,64,99,56],[98,36,78,44,8,99,71,86,87,69,60,61,48,39,35,32,7,100,29,19,15,85,66,9,41,59,22,13,79,11,77,12,0,25,93,42,33,53,2,6,94,64,95,73,16],[62,12,30,100,90,81,23,72,39,10,13,78,74,15,18,4,76,47,73,70,24,19,45,61,63,65,99,60,98,20,5,34,52,14,95,54,66,55,91,94,71,83,2,50,59],[7,38,29,97,98,66,3,39,55,74,64,41,30,60,6,73,100,53,52,84,67,78,47,72,63,46,43,40,5,56,62,59,36,94,51,54,37,80,33,17,34,75,20,50,68],[69,35,91,67,82,0,73,94,98,40,56,48,22,17,4,14,24,64,34,84,92,55,5,88,45,31,93,96,54,59,26,60,11,53,50,58,65,12,25,18,77,74,10,72,20],[69,49,81,100,5,58,21,82,23,85,7,4,52,11,26,86,1,63,41,34,13,65,68,43,12,78,32,79,93,0,83,15,27,54,47,42,97,39,72,33,60,64,88,45,3],[7,29,10,63,33,51,47,90,98,99,28,75,41,12,56,91,88,62,68,52,13,16,20,77,19,94,17,6,43,67,26,69,37,89,34,40,49,64,78,46,42,27,93,57,38],[80,75,2,40,67,49,99,73,52,68,33,53,20,96,54,34,10,58,38,86,26,92,24,56,74,47,14,89,4,81,23,5,84,46,27,91,70,55,35,16,87,7,97,29,22],[3,2,58,36,80,43,8,42,46,84,17,6,100,51,66,95,69,18,15,53,57,47,52,12,76,71,70,40,25,37,87,29,41,81,39,26,89,48,33,24,55,22,79,63,31],[63,41,45,20,35,77,78,57,33,62,48,80,84,91,10,22,19,40,53,55,65,59,83,23,94,24,27,60,11,56,92,73,97,64,17,47,13,44,4,38,39,75,58,76,89],[49,69,55,90,72,28,81,32,47,91,98,29,30,67,20,26,78,89,31,77,12,83,99,23,43,1,11,68,56,38,61,62,15,74,76,73,79,9,0,25,65,19,57,96,50],[67,20,16,4,42,55,13,10,36,41,77,29,91,87,40,21,93,44,56,92,1,9,12,46,68,7,81,6,84,99,66,27,95,19,100,35,2,72,98,43,75,0,47,74,31],[63,64,4,22,96,50,0,23,60,8,80,1,56,5,82,36,73,92,67,35,65,84,79,83,46,37,9,14,54,15,71,24,13,53,99,3,58,55,21,29,25,2,87,59,51],[51,90,24,37,49,68,20,83,13,21,65,73,15,47,17,30,57,38,26,40,8,82,92,35,10,29,44,81,56,100,59,6,88,89,16,39,1,93,76,71,4,61,97,33,32],[90,2,7,73,98,67,100,70,93,22,71,66,92,96,57,41,99,74,21,32,34,10,5,42,95,58,1,30,0,49,69,54,79,46,44,18,97,13,3,23,89,35,68,4,6],[20,25,78,28,90,11,18,24,66,65,58,1,100,3,51,79,91,12,83,98,67,96,39,86,82,41,16,40,43,32,38,23,63,97,5,73,56,70,19,71,75,92,15,60,4],[29,13,26,48,22,40,49,30,89,27,95,19,35,83,8,47,9,78,80,82,7,21,32,2,72,71,62,38,90,6,45,53,31,59,52,50,92,34,4,42,99,87,65,33,41],[23,17,29,55,84,70,73,10,37,88,69,11,71,45,1,52,85,5,3,67,64,25,62,74,20,54,42,15,65,80,92,57,60,86,98,16,100,36,93,89,50,63,79,61,47],[73,99,4,24,29,100,66,92,67,32,0,1,25,23,59,62,56,44,22,58,34,9,46,33,75,71,5,6,64,95,41,48,19,93,45,15,39,94,2,55,49,53,78,31,72],[2,34,83,43,75,73,51,13,60,57,5,81,96,90,28,22,59,19,61,24,20,49,27,53,9,39,45,8,7,70,36,35,66,15,6,58,91,52,98,18,14,17,67,87,74],[33,61,10,6,52,70,53,11,39,75,4,22,47,36,79,74,67,97,65,72,57,86,91,21,17,83,16,3,19,90,48,60,0,45,98,63,20,87,66,64,32,1,56,73,30],[25,73,43,20,17,3,100,15,49,69,37,99,11,48,21,24,44,78,5,83,98,29,2,34,14,10,38,56,62,40,36,6,1,23,87,60,4,31,86,94,66,30,74,77,59],[85,18,37,10,2,79,57,60,11,48,22,81,44,19,62,95,5,7,69,15,46,52,3,41,39,75,88,31,67,100,89,82,74,87,92,93,58,66,6,86,72,77,80,99,64],[30,18,40,70,90,83,75,52,45,89,5,85,13,73,7,6,94,15,74,92,2,59,37,84,38,54,55,93,66,8,51,87,10,86,1,28,49,41,64,100,67,68,65,26,95],[99,51,66,37,41,69,23,15,89,26,35,39,17,10,72,48,5,18,28,63,76,50,55,42,33,68,97,59,7,2,8,40,30,74,100,24,91,31,70,64,0,47,3,56,85],[7,77,22,87,84,72,20,89,47,88,78,85,64,82,94,95,0,34,73,66,24,50,42,30,9,6,12,75,69,38,1,2,28,40,62,21,83,67,35,53,61,86,60,59,18],[8,41,62,99,23,92,89,22,38,7,56,86,100,63,73,77,74,98,65,6,37,43,84,35,50,95,61,94,42,10,16,4,83,60,51,96,75,34,67,0,48,54,66,33,69],[82,77,8,12,76,69,96,47,7,10,9,22,87,93,43,33,48,90,63,45,32,26,79,51,3,98,44,46,86,97,94,4,72,1,14,60,66,11,56,34,61,31,25,53,23],[83,87,42,21,20,34,98,0,58,47,100,40,33,99,66,45,69,37,52,61,24,88,78,14,90,76,68,79,23,29,73,81,26,50,32,5,63,2,18,35,8,59,94,3,67],[62,66,88,49,35,13,24,29,90,51,98,95,14,57,20,74,21,69,91,53,60,87,56,86,33,54,10,100,12,75,39,45,9,3,94,85,23,30,47,46,55,99,50,7,43],[6,24,83,20,67,59,48,21,81,11,99,87,95,17,46,96,18,58,77,93,89,26,37,86,22,100,56,79,90,27,44,8,78,28,33,35,75,25,74,88,15,40,49,30,84]],4749)
    
def main():
    tests()
    print("All tests passed.")

if __name__ == "__main__":
    main()