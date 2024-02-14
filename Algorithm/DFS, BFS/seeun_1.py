class Solution(object):
    def sumNumbers(self, root):
        def dfs(node, now_sum):
            if not node:
                return 0

            now_sum = now_sum * 10 + node.val

            if not node.left and not node.right:
                return now_sum

            left = dfs(node.left, now_sum)
            right = dfs(node.right, now_sum)

            return left + right

        if not root:
            return 0

        return dfs(root, 0)
