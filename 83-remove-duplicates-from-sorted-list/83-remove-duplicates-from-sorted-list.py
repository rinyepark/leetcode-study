# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        if head == None:
            return ListNode("",None)
        
        cur = head
        answer = ListNode()
        link = answer
        val = -101
        
        while True:
            if cur == None:
                break
            if cur.val != val:
                link.next = ListNode(cur.val, None)
                link = link.next
                val = cur.val
            cur = cur.next
        return answer.next
                
        