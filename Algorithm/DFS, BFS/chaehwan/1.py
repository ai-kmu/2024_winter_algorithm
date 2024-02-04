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

2번 풀이, 내려갈 때마다 문자열이 "4", "49", "495"로 변하고 leaf이면 int형으로 바꿔서 finals에 저장 후, 다 돈 다음에 finals 합치기
# class Solution(object):
#     def sumNumbers(self, root):

#         finals = []
#         def untilLeaf(node, relay):
#             relay += str(node.val)
#             if node.left is None and node.right is None:
#                 finals.append(int(relay))
#             if node.left is not None:
#                 untilLeaf(node.left, relay)
#             if node.right is not None:
#                 untilLeaf(node.right, relay)

#         untilLeaf(root, "")
#         res = sum(finals)
#         return res
        
