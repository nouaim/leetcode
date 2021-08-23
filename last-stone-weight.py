## The problem can be found here https://leetcode.com/problems/last-stone-weight/

import numpy as np
class Solution:


    def lastStoneWeight(self, stones):

        b=[0]*2
        a= np.max(stones)
        
        

        while (  len(stones)>1 ): 
            for i in range (0,2) :
                a= np.max(stones)
                b[i] = a
                stones.remove(a)
            S= b[0] - b[1]
            stones.append(S)
    		
        len(stones)

        return(stones[0])