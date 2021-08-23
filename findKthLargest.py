import numpy as np


class Solution:

    def findKthLargest(nums, k):

        for i in range(0, k):
            a = np.max(nums)
            nums.remove(a)
        return a

    
    
    
    ####print(findKthLargest([4, 5, 8, 41],2))
