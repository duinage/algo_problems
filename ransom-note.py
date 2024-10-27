# PROBLEM DESCRIPTON: https://leetcode.com/problems/ransom-note/description/
# SOLUTION SUMBITION: https://leetcode.com/problems/ransom-note/submissions/1435577482/
from collections import Counter

class Solution_1:
    # 19 ms
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = dict()
        for letter in magazine:
            hash_map[letter] = hash_map.get(letter, 0) + 1

        for letter in ransomNote:
            if letter in hash_map:
                if hash_map[letter] <= 0:
                    return False
                hash_map[letter] -= 1
            else:
                return False
        
        return True
    
class Solution_2:
    # 15 ms
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = Counter(magazine)

        for letter in ransomNote:
            if letter in hash_map:
                if hash_map[letter] <= 0:
                    return False
                hash_map[letter] -= 1
            else:
                return False
        
        return True

def tests():
    s = Solution_1()
    assert s.canConstruct("a", "b") == False
    assert s.canConstruct("aa", "ab") == False
    assert s.canConstruct("aa", "aab") == True

    s = Solution_2()
    assert s.canConstruct("a", "b") == False
    assert s.canConstruct("aa", "ab") == False
    assert s.canConstruct("aa", "aab") == True

def main():
    tests()
    print("All tests passed.")

if __name__ == "__main__":
    main()