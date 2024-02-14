class Solution(object):
    def sumNumbers(self, root):
        if not root:
            return 0
        
        total_sum = 0
        lst = [(root, root.val)]
        
        while len(lst) != 0:
            node, now_sum = lst.pop()
            
            if not node.left and not node.right:
                total_sum += now_sum
            
            if node.right:
                lst.append((node.right, now_sum * 10 + node.right.val))
            
            if node.left:
                lst.append((node.left, now_sum * 10 + node.left.val))
        
        return total_sum
