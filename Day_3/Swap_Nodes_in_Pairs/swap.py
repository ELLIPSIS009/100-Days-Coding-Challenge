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