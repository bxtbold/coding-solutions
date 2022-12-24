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
class BetterSolution {
public:
    /**
     * RUNTIME: 24 ms (98.71%)
     * MEMORY: 71.4 MB (82.78%)
    */
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *sum = new ListNode();
        ListNode *handle = sum;
        unsigned prev = 0;
        while (l1 != NULL || l2 != NULL) {
            // add values
            if (l1 != NULL && l2 != NULL) {
                prev = l1->val + l2->val + prev;
            }
            else if (l1 == NULL && l2 != NULL) {
                prev = l2->val + prev;
            }
            else if (l2 == NULL && l1 != NULL) {
                prev = l1->val + prev;
            }
            else {
                break;
            }
            // traverse handle
            if (l1 != NULL) {
                l1 = l1->next;
            }
            if (l2 != NULL) {
                l2 = l2->next;
            }
            // create a new node
            ListNode *newNode = new ListNode(prev % 10);
            handle->next = newNode;
            handle = handle->next;
            prev /= 10;
        }
        if (prev != 0) {
            ListNode *newNode = new ListNode(prev);
            handle->next = newNode;
        }
        return sum->next;
    }
};

class Solution {
public:
    /**
     * RUNTIME: 41 ms (83.31%)
     * MEMORY: 71.5 MB (52.29%)
    */
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *sum = new ListNode();
        ListNode *handle = sum;
        unsigned tmp, add = 0;
        while (l1 != NULL or l2 != NULL) {
            // create a new node
            ListNode *newNode = new ListNode();
            handle->next = newNode;
            handle = handle->next;
            if (l1 != NULL && l2 != NULL) {
                // add values
                tmp = l1->val + l2->val + add;
                add = 0;
                if (tmp >= 10) {
                    add = tmp / 10;
                    tmp = tmp % 10;
                }
                // traverse nodes
                l1 = l1->next;
                l2 = l2->next;
            }
            else if (l1 == NULL && l2 != NULL) {
                // add values
                tmp = l2->val + add;
                add = 0;
                if (tmp >= 10) {
                    add = tmp / 10;
                    tmp = tmp % 10;
                }
                // traverse nodes
                l2 = l2->next;
            }
            else if (l2 == NULL && l1 != NULL) {
                // add values
                tmp = l1->val + add;
                add = 0;
                if (tmp >= 10) {
                    add = tmp / 10;
                    tmp = tmp % 10;
                }
                // traverse nodes
                l1 = l1->next;
            }
            handle->val = tmp;
        }
        if (add > 0) {
            ListNode *newNode = new ListNode(add);
            handle->next = newNode;
        }
        return sum->next;
    }
};
