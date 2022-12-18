/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * RUNTIME: 11 ms (90.91%)
     * MEMORY: 8 MB (82.46%)
    */
    bool hasCycle(ListNode *head) {
        if (!head || !head->next || !head->next->next) {
            return false;
        }
        ListNode* slow = head->next;
        ListNode* fast = head->next->next;
        while (slow != fast) {
            if (!fast->next || !fast->next->next) {
                return false;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        return true;
    }
};
