# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper function to reverse a portion of the list
        def reverseLinkedList(head: ListNode, k: int) -> ListNode:
            new_head, ptr = None, head
            while k:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k -= 1
            return new_head
        
        # Count the length of the linked list
        count = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            count += 1
        
        # Dummy node initialization
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Process the list in chunks of size k
        while count >= k:
            current = prev.next
            # Store the next node after the k nodes
            tail = current
            for _ in range(k - 1):
                tail = tail.next
            next_group = tail.next
            
            # Reverse the next k nodes
            prev.next = reverseLinkedList(current, k)
            current.next = next_group
            
            # Move prev to the end of the reversed section
            prev = current
            count -= k
        
        return dummy.next