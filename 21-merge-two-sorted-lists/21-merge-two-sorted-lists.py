# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        answer = ListNode()
        last_node = answer
        
        while list1 != None or list2 != None:
            
            #둘 다 있는 경우 -> 비교
            if list1 == None:
                tmp = ListNode(list2.val)
                list2 = list2.next
                
            elif list2 == None:
                tmp = ListNode(list1.val)
                list1 = list1.next
                
            else:
                if list1.val <= list2.val:
                    tmp = ListNode(list1.val)
                    list1 = list1.next
                    
                else:
                    tmp = ListNode(list2.val)
                    list2 = list2.next
    
            last_node.next = tmp
            last_node = last_node.next
        
        answer = answer.next
        return answer
                    
                
                
            