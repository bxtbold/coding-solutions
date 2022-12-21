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
     * RUNTIME: 31 ms (73.75%)
     * MEMORY: 15 MB (81.27%)
    */
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *tmp;
        while (head && head->val == val) {
            tmp = head->next;
            head = tmp;
        }
        if (!head) { return NULL; }
        ListNode *current = head;
        while (current->next) {
            if (current->next->val == val) {
                current->next = current->next->next;
            }
            else {
                current = current->next;
            }
        }
        return head;
    }
};