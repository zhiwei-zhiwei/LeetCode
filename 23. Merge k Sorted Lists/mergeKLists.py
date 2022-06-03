# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        dummy = ListNode(-1)
        check = dummy
        temp = []
        for i in range(len(lists)):
            if lists[i]: # make sure that the current list is not empty
                heapq.heappush(temp,(lists[i].val, i))
                # the temp array will sort the lists by the first num
                # eg: [[4,6,8],[1,3,4],[3,6]] --> [(1, 1), (4, 0), (3, 2)]
                lists[i] = lists[i].next # move to the next and append that into temp

        while temp:
            val, index = heapq.heappop(temp)
            # [(1, 1), (4, 0), (3, 2)]
            # val   index
            # 1     1
            # 3     2
            # 4     0
            check.next = ListNode(val)
            check = check.next
            if lists[index]:
                # check the current list and push into the dummy list
                heapq.heappush(temp,(lists[index].val,index))
                lists[index] = lists[index].next
        return dummy.next
