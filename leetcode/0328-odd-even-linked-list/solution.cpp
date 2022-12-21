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
     * RUNTIME: 12 ms (88.18%)
     * MEMORY: 11.1 MB (5.19%)
    */
    ListNode* oddEvenList(ListNode* head) {
        if (!head) return NULL;
        if (head->next == NULL || head->next->next == NULL) return head;
        ListNode *result = new ListNode();
        ListNode *res_copy = result, *current = head;
        while (true) {
            res_copy->val = current->val;
            ListNode *tmp = new ListNode();
            res_copy->next = tmp;
            if (current->next == NULL || current->next->next == NULL) { break; }
            current = current->next->next;
            res_copy = res_copy->next;
        }
        current = head->next;
        while (true) {
            ListNode *tmp = new ListNode(current->val);
            res_copy->next = tmp;
            if (current->next == NULL || current->next->next == NULL) { break; }
            current = current->next->next;
            res_copy = res_copy->next;
        }
        return result;
    }
};
