# PROBLEM DESCRIPTON: https://leetcode.com/problems/middle-of-the-linked-list/description/
# SOLUTION SUMBITION: https://leetcode.com/problems/middle-of-the-linked-list/submissions/1435333214/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle_node = head 
        middle_index = 0

        pointer = head
        last_index = 0
        
        while pointer.next:
            pointer = pointer.next
            if last_index / 2 >= middle_index:
                middle_index += 1
                middle_node = middle_node.next
            last_index += 1

        return middle_node

def test1():
    head5 = ListNode(5)
    head4 = ListNode(4, head5)
    head3 = ListNode(3, head4)
    head2 = ListNode(2, head3)
    head1 = ListNode(1, head2)

    head = head1
    s = Solution()
    assert s.middleNode(head).val == 3

def test2():
    linked_list_values = [1,2,3,4,5,6]
    head = ListNode(linked_list_values[-1])
    for value in linked_list_values[-2::-1]:
        next = head
        head = ListNode(value, next)

    s = Solution()
    assert s.middleNode(head).val == 4


def tests():
    test1()
    test2()

def main():
    tests()
    print("All tests passed.")

if __name__ == "__main__":
    main()