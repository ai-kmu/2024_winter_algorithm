"""
LeetCode
129. Sum Root to Leaf Numbers
(https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)

tree의 root부터 leaf까지의 값을 일정한 규칙으로 치환한 후 값의 합을 구함.

가령 1(root) -> 2-> 3(leaf) 라면 123 과 같은 방식으로 수로 치환한 후 
가능한 모든 root -(...)-> leaf를 치환하여 얻은 값들의 합을 구함.

=======
example.
=======
tree

         4
    9       0
5      1

root --> leaf
4 -> 9 -> 5   => 495
4 -> 9 -> 1   => 491
4 -> 0        => 40

result
495 + 491 + 40 = 1026

output
1026

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    #===============
    # sub function
    #===============
    """
    :input: TreeNode node(현재 탐색중인 node)
    :output: bool (현재 node의 leaf 여부)

    :설명: 주어진 node(TreeNode node)가 tree의 leaf인지 판정하는 함수
    """
    def isLeaf(self,node):

        if node.left or node.right:#다음 node정보가 있다면 leaf node가 아님.
            return False
        else:
            return True

    """
    :input: list stack (tree의 root부터 leaf까지의 값을 저장한 stack)
    :output: int result(주어진 stack을 통해 얻은 값)

    :설명: 주어진 stack(list stack)을 통해 root값부터 leaf값까지의 수를 
        정해진 규칙을 통해 적절한 수로 치환하는 함수
        ex. 1(root) -> 2-> 3(leaf)   =>  123 , 
            1(root) -> 6-> 5 -> 7(leaf)   =>  1657 
    """
    def sumStack(self,stack):

        depth = len(stack)-1
        result = 0
        for node in stack:

            result+= node.val * 10**depth
            depth -= 1

        return result

    #===============
    # main function
    #===============
    """
    :input: TreeNode root(주어진 tree의 root node) 
    :output: int result(규칙에 맞게 치환된 수의 총 합)

    :설명: 주어진 tree의 root부터 leaf까지의 값을 숫자로 치환한 값들의 
        총 합을 구하는 함수
    """
    def sumNumbers(self, root):
        
        result = 0 #총 합
        stack =[root]
        crr = root #현재 탐색중인 node

        while True:

            #leaf node까지 탐색하여 stack에 저장
            while not(self.isLeaf(crr)):

                #다음 탐색방향을 정하고 이미 지나간 길은 지워줌.
                if not(crr.left):
                    tmp = crr.right
                    crr.right = None 
                else:
                    tmp = crr.left
                    crr.left = None

                #다음 탐색지로 이동    
                crr = tmp
                stack.append(crr)

            '''stack에 저장된 root에서 현재 leaf까지의 node정보를 이용하여
            숫자를 얻어 result에 더함.'''
            result += self.sumStack(stack)

            #탐색이 완료된 node를 버리고 다음 탐색지 정보를 가진 node 탐색
            while self.isLeaf(crr):

                if len(stack)==0:#root node까지 탐색이 완료됐을때 종료
                    return result
                
                crr = stack.pop()

            stack.append(crr)#다음 탐색지 정보를 가진 node를 다시 stack에 넣어줌.
