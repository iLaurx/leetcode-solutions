/*

? 2. Add two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

*/

#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {} 
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0); // Nodo temporal en la pila
        ListNode* curr = &dummy; // 'curr' empieza apuntando a dummy
        int acarreo = 0;

        while (l1 != nullptr || l2 != nullptr || acarreo != 0)
        {
            int x = (l1 != nullptr) ? l1->val : 0;

            int y = (l2 != nullptr) ? l2->val : 0;

            int suma = x + y + acarreo;

            acarreo = suma / 10;

            // Nuevo nodo con residuo (digito resultante)
            curr->next = new ListNode(suma % 10);

            curr = curr->next;

            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;

        }
        return dummy.next;
    }
};

int main() {

    ListNode* l1 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9)))))));
    ListNode* l2 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))));

    Solution mySolution;

    ListNode* resultado =  mySolution.addTwoNumbers(l1, l2);

    std::cout << "[";
    while (resultado != nullptr) {
        
        std::cout << resultado->val;
        if (resultado->next != nullptr) std::cout << ",";
        resultado = resultado->next;
    }
    std::cout << "]";
    std::cout << std::endl;

    return 0;

}