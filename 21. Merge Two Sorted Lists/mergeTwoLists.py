# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # ----------------------------Brute force---------------------------
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        check = dummy
        while list1 and list2:
            if list1.val < list2.val:
                check.next = list1
                list1 = list1.next
            else:
                check.next = list2
                list2 = list2.next
            check = check.next

        check.next = list1 if list1 is not None else list2
        # at the end of the seaching, there is one list is empty but still have one element doesnt
        # put into the dummy list yet, so here to check the last one

        return dummy.next
    # ----------------------------Brute force---------------------------


    # ----------------------------Recursion-----------------------------
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2  
        # stop recursion as long as one of the list is empty
        if not list2: return list1  
        # then retrun the rest of another list
        
        if list1.val <= list2.val:  
            # recursion
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2
    # ----------------------------Recursion-----------------------------

    