class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestBSTSubtreeSum(root):
    def helper(node):
        if not node:
            return True, 0, float('inf'), float('-inf')
        
        is_left_bst, left_sum, left_min, left_max = helper(node.left)
        is_right_bst, right_sum, right_min, right_max = helper(node.right)
        
        if is_left_bst and is_right_bst and left_max < node.val < right_min:
            curr_sum = node.val + left_sum + right_sum
            max_sums[0] = max(max_sums[0], curr_sum)
            return True, curr_sum, min(left_min, node.val), max(right_max, node.val)
        
        return False, 0, 0, 0

    max_sums = [0]
    helper(root)
    return max_sums[0]

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(2)
root.right.right.right = TreeNode(5)
root.right.right.right.left = TreeNode(4)
root.right.right.right.right = TreeNode(6)

print(largestBSTSubtreeSum(root))  # Output: 20
