'''
Platform :- Leetcode
Problem :- Increasing Order Search Tree
Link :- https://leetcode.com/problems/increasing-order-search-tree/description/

Problem statement :- Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree,
                     and every node has no left child and only one right child.

Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:
Input: root = [5,1,7]
Output: [1,null,5,null,7]
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(root):
        tree = []
        if root:
            tree = Solution.inorder(root.left)
            tree.append(root.val)
            tree += Solution.inorder(root.right)
        return tree

    def increasingBST(root):
        if root is None: 
            return root
        elif root.right == None and root.left == None:
            return root
        else:
            temp = TreeNode()
            tree = Solution.inorder(root)
            for i in range(len(tree)):
                if i == 0:
                    z = TreeNode(tree[i])
                    temp = z
                    root = z
                else:
                    z = TreeNode(tree[i])
                    temp.right = z
                    temp = z
        return root

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)
print(Solution.inorder(Solution.increasingBST(root)))