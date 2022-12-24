/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    /**
     * RUNTIME: 4 ms (81.75%)
     * MEMORY: 7.3 MB (63.12%)
    */
    Node* flatten(Node* head) {
        Node *curr;
        curr = head;
        while (curr != NULL) {
            if (curr->child != NULL) {
                getChild(curr, curr->child, curr->next);
                curr->child = NULL;
            }
            curr = curr->next;
        }
        return head;
    }

    void getChild(Node* before, Node* child, Node* after) {
        // bind before to child
        before->next = child;
        // bind child to before
        child->prev = before;
        // bind child's lastNode to after
        Node *lastNode;
        lastNode = child;
        while (child != NULL) {
            if (child->child != NULL) {
                getChild(child, child->child, child->next);
                child->child = NULL;
            }
            lastNode = child;
            child = child->next;
        }
        lastNode->next = after;
        // bind after to child's lastNode
        if (after != NULL) {
            after->prev = lastNode;
        }
    }
};
