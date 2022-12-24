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
     * RUNTIME: 3 ms (98.86%)
     * MEMORY: 14.8 MB (44.21%)
    */
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == NULL) { return list2; }
        if (list2 == NULL) { return list1; }
        ListNode *handle1 = list1, *handle2 = list2;
        ListNode *merged = new ListNode();
        ListNode *handleMerged = merged;
        while (true) {
            if (handle1 != NULL && handle2 != NULL) {
                ListNode *tmp = new ListNode();
                handleMerged->next = tmp;
                handleMerged = handleMerged->next;
                if (handle1->val < handle2->val) {
                    handleMerged->val = handle1->val;
                    handle1 = handle1->next;
                }
                else if (handle2->val < handle1->val) {
                    handleMerged->val = handle2->val;
                    handle2 = handle2->next;
                }
                else if (handle1->val == handle2->val) {
                    handleMerged->val = handle1->val;
                    ListNode *tmp = new ListNode(handle2->val);
                    handleMerged->next = tmp;
                    handleMerged = handleMerged->next;
                    handle1 = handle1->next;
                    handle2 = handle2->next;
                }
            }
            else if (handle1 == NULL) {
                handleMerged->next = handle2;
                break;
            }
            else if (handle2 == NULL ) {
                handleMerged->next = handle1;
                break;
            }
        }
        return merged->next;
    }
};
