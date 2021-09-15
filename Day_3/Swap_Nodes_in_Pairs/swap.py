'''
Platform :- Leetcode
Problem :- Swap Nodes in Pairs
Link :- https://leetcode.com/problems/swap-nodes-in-pairs/

Problem statement :- Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def tree(root):
        tree = []
        if root:
            tree.append(root.val)
            tree += Solution.tree(root.next)
        return tree

    def swapPairs(root):
        temp = ListNode()
        temp.next = root
        current = temp
        while current.next is not None and current.next.next is not None:
            first = current.next
            second = current.next.next
            first.next = second.next
            current.next = second
            current.next.next = first
            current = current.next.next
        return temp.next


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)

print(Solution.tree(Solution.swapPairs(root)))