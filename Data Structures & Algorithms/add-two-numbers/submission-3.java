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
        ListNode root = new ListNode(l1.val + l2.val);

        int carry = 0;
        if (root.val >= 10) {
            root.val -= 10;
            carry = 1;
        }

        ListNode curr = root;

        while (l1.next != null || l2.next != null) {
            ListNode next = new ListNode(0);
            if (l1.next != null) {
                next.val += l1.next.val;
                l1 = l1.next;
            }
            if (l2.next != null) {
                next.val += l2.next.val;
                l2 = l2.next;
            }
            if (carry > 0) {
                next.val += carry;
                carry = 0;
            }
            if (next.val >= 10) {
                carry = 1;
                next.val -= 10;
            }
            curr.next = next;
            curr = curr.next;

        }
        if (carry != 0) {
            curr.next = new ListNode(carry);
        }


        return root;
    }
}
