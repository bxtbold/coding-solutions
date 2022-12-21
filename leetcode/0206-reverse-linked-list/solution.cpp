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
     * RUNTIME: 3 ms (98.73%)
     * MEMORY: 8.3 MB (80.16%)
    */
    ListNode* reverseList(ListNode* head) {
        ListNode *tmp, *reversed_list = NULL;
        while (head) {
            tmp = head->next;
            head->next = reversed_list;
            reversed_list = head;
            head = tmp;
        }
        return reversed_list;
    }
};
