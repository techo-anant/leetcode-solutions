// Question desc

// You are given the heads of two sorted linked lists list1 and list2.

// Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

// Example 2:

// Input: list1 = [], list2 = []
// Output: []
// Example 3:

// Input: list1 = [], list2 = [0]
// Output: [0]


// Constraints:

// The number of nodes in both lists is in the range [0, 50].
// -100 <= Node.val <= 100
// Both list1 and list2 are sorted in non-decreasing order.


// Solution

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    if (!list1 && !list2) return null;
    if (!list1) return list2;
    if (!list2) return list1;

    let newList: ListNode | null = null;
    let startNode: ListNode | null = null;

    while (list1 && list2) {
        if (list1.val <= list2.val) {
            if (!newList) {
                newList = new ListNode(list1.val);
                list1 = list1.next;
                startNode = newList
                continue;
            }
            let newNode: ListNode | null = new ListNode(list1.val);
            newList.next = newNode;
            newList = newList.next;
            list1 = list1.next;
        } else {
            if (!newList) {
                newList = new ListNode(list2.val);
                list2 = list2.next;
                startNode = newList
                continue;
            }
            let newNode: ListNode | null = new ListNode(list2.val);
            newList.next = newNode;
            newList = newList.next;
            list2 = list2.next;
        }
    }

    if (list1) {
        newList.next = list1;
    } else {
        newList.next = list2;
    }

    return startNode;
};