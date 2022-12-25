/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    /**
     * RUNTIME: 11 ms (71.90%)
     * MEMORY: 11.9 MB (7.20%)
    */
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL) { return NULL; }
        if (head->next == NULL || k == 0) { return head; }

        // get size
        ListNode *fast, *slow;
        fast = head;
        int size = 0;
        while (fast != NULL) {
            fast = fast->next;
            size++;
        }
        k = k % size;
        if (k == 0) { return head; }

        // set two pointers
        fast = slow = head;
        for (int i=0; i < k; i++) {
            fast = fast->next;
        }

        // traverse til the end of the linked list
        ListNode *result = new ListNode();
        ListNode *handle;
        handle = result;
        while (fast != NULL) {
            ListNode *tmp = new ListNode(slow->val);
            handle->next = tmp;
            fast = fast->next;
            slow = slow->next;
            handle = handle->next;
        }
        result = result->next;

        // move slow to the head
        ListNode *cur;
        cur = slow;
        while (cur->next != NULL) {
            cur = cur->next;
        }
        cur->next = result;
        return slow;
    }
};
