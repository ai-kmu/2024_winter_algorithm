from collections import deque

def sumRelay(upperSum,node):
    
    if node.left and node.right:
        return sumRelay(upperSum*10+node.val, node.left)+sumRelay(upperSum*10+node.val, node.right)
    elif node.left:
        return sumRelay(upperSum*10+node.val, node.left)
    elif node.right:
        return sumRelay(upperSum*10+node.val, node.right)
    else:
        return upperSum*10+node.val

class Solution(object):
    def sumNumbers(self, root):return sumRelay(0, root)


# class Solution(object):
#     def sumNumbers(self, root):

#         finals = []
#         def untilLeaf(node, relay):
#             relay += str(node.val)
#             if node.left is None and node.right is None:
#                 finals.append(relay)
#             if node.left is not None:
#                 untilLeaf(node.left, relay)
#             if node.right is not None:
#                 untilLeaf(node.right, relay)

#         untilLeaf(root, "")
#         res = 0
#         for x in finals:
#             relay += int(x)
#         return res
        
