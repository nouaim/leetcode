## https://leetcode.com/problems/middle-of-the-linked-list/s

class Solution(object):
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[int(len(A) / 2)]