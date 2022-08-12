# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    tmp_cur = ListNode()
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        r_head = ListNode()
        cur = head
        tmp_cur = r_head
        
        if cur != None:
            self.recurse(cur, tmp_cur)
        
            return r_head.next
        else:
            return ListNode('')
        
            
    def recurse(self, cur, tmp_cur):
        
        if cur.next == None:
            tmp_cur.next = cur
            tmp_cur = tmp_cur.next
            return tmp_cur
        
        tmp_cur = self.recurse(cur.next, tmp_cur)
        tmp_node = ListNode(cur.val, None)
        
        tmp_cur.next = tmp_node 
        tmp_cur = tmp_cur.next
        
        return tmp_cur