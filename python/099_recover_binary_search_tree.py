# https://leetcode.com/problems/recover-binary-search-tree/

# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        list = []
        listnode = []
        self.inorder(root, list, listnode)
        list.sort()
        for i in range(len(list)):
            listnode[i].val = list[i]
            
        
    def inorder(self, root, list, listnode):
        if root:
            self.inorder(root.left, list, listnode)
            list.append(root.val)
            listnode.append(root)
            self.inorder(root.right, list, listnode)
            