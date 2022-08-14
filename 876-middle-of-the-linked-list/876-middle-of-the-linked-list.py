# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 총 node의 개수 파악
        cnt = 0
        cur = head
        while cur != None:
            cnt += 1
            cur = cur.next
        
        move = cnt // 2
        
        
        answer = head
        while move > 0:
            move -= 1
            answer = answer.next
        
        return answer
        