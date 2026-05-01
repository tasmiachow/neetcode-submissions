# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # go through both lists
        # if currList1> currList2:
        # merger pointer 
        # only move one pointer in the list if its < 

        if list1 == None:
            return list2
        elif list2 == None:
            return list1 
        
        curr1 = list1
        curr2 = list2
        mergePointer=ListNode()
        tail = mergePointer
        while(curr1 or curr2):
            if(curr1==None):
                tail.next =curr2
                curr2 = curr2.next
                tail = tail.next
            elif(curr2 == None):
                tail.next =curr1
                curr1 = curr1.next
                tail = tail.next
            elif(curr1.val<=curr2.val):
                tail.next = curr1
                curr1 = curr1.next
                tail = tail.next
            elif(curr2.val<curr1.val): 
                tail.next = curr2
                curr2 = curr2.next
                tail = tail.next

        return mergePointer.next
            