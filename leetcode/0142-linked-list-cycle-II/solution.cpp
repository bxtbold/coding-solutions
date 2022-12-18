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
     * RUNTIME: 17 ms (60.40%)
     * MEMORY: 9.2 MB (22.16%)
    */
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next || !head->next->next) {
            return NULL;
        }
        unordered_map <ListNode*, int> slowTraversed;
        slowTraversed[head] = 0;
        ListNode* slow = head->next;
        ListNode* fast = head->next->next;
        while (slow != fast) {
            slowTraversed[slow] = 0;
            if (!fast->next || !fast->next->next) {
                return NULL;
            }
            if (slowTraversed.find(fast) != slowTraversed.end()) {
                return fast;
            }
            else if (slowTraversed.find(fast->next) != slowTraversed.end()) {
                return fast->next;
            }
            if (slowTraversed.find(fast->next->next) != slowTraversed.end()) {
                return fast->next->next;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        return fast;
    }
};