class Solution(object):
    def findMid(self, n, left, right):
        mid = (left+right) //2
        stairN = mid*(mid+1)//2
        print(left,mid,right)
        if stairN < n and left<mid:
            return self.findMid(n,mid,right)
        elif stairN > n:
            return self.findMid(n,left,mid)
        else:
            return mid


    def arrangeCoins(self, n):
        return self.findMid(n,1,n)   