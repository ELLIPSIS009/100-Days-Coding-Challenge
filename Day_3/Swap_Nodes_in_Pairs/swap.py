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
        tree = Solution.tree(root)
        for i in range(0, len(tree), 2):
            tree[i], tree[i+1] = tree[i+1], tree[i]
        return tree

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
print(Solution.swapPairs(root))
        