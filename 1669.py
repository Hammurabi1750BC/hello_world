# 1669	Merge In Between Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1, list1)
        node = dummy
        
        for _ in range(a):
            node = node.next
        list1dex = a

        temp = node.next
        list1dex += 1
        node.next = list2
        node = temp
        
        for _ in range(list1dex, b+1):
            node = node.next
        
        list2node = list2
        while list2node.next:
            list2node = list2node.next
            
        list2node.next = node.next
        
        return dummy.next
