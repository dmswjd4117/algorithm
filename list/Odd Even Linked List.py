# https://leetcode.com/problems/odd-even-linked-list/submissions/



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def oddEvenList(self, head):
        
        if not head:
            return head
        
        odd_tail = head
        
        even_head = head.next
        
        
        index = 1
        cur = head
        while True:
            if index % 2 != 0:
                odd_tail = cur
            index += 1
            
            if not cur.next: break
            nnode = cur.next
            cur.next = nnode.next
            cur = nnode
            
        odd_tail.next = even_head
        
        
            
        return head