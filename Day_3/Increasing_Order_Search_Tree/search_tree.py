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
        # elif root.left == None and root.right == None:
        #     return
        # else:
        #     tree.append('null')
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