# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        
        cur = l1
        while cur != None:
            num1 += str(cur.val)
            cur = cur.next
        
        cur = l2
        while cur != None:
            num2 += str(cur.val)
            cur = cur.next
        
        num = str(int(num1[::-1]) + int(num2[::-1]))
        
        answer = ListNode()
        cur = answer
        
        for i in range(len(num)-1, -1, -1):
            cur.next = ListNode(int(num[i]))
            cur = cur.next
        
        return answer.next
        