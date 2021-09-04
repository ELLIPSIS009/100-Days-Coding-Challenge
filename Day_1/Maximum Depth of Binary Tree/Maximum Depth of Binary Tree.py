# Problem : https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(root):
        if root is None:
            return 0
        else:
            ldep = Solution.maxDepth(root.left)
            rdep = Solution.maxDepth(root.right)
            
            if ldep > rdep:
                return ldep + 1
            else:
                return rdep + 1

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.left.left = TreeNode(None)
# root.left.right = TreeNode(None)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

def createTree(root, tree, index, n):
    root.left = TreeNode(tree[index])
    root.right = TreeNode(tree[index + 1])

tree = list(input('Enter the nodes of binary tree: ').split(' '))
root = TreeNode(tree[0])
index = 1
count = 0
while True:
    root.left = createTree(root, tree, index, )
    index += 2**count
    count += 1


print(f'Max Depth of this Binary tree is : {Solution.maxDepth(root)}')
