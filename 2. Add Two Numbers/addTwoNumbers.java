/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode root = new ListNode(0); // fist position of the linked list and set as the root
        ListNode newList = root;
        int extraNum = 0; // to deal with the condition that sum of two number is bigger than 9
        while(l1 != null || l2 != null || extraNum != 0) {
            // take example 3 as a special one
            //  l1 [9,9,9,9,9,9,9]
            //  l2 [9,9,9,9]
            // sol [8,9,9,9,0,0,0,1]
            int l1Val = l1 != null ? l1.val : 0;
            int l2Val = l2 != null ? l2.val : 0;
            int sumNum = l1Val + l2Val + extraNum;
            extraNum = sumNum / 10;
            ListNode sumNode = new ListNode(sumNum % 10);
            newList.next = sumNode;
            newList = sumNode;

            if(l1 != null)
                l1 = l1.next;
            if(l2 != null)
                l2 = l2.next;
        }
        return root.next;
    }
}