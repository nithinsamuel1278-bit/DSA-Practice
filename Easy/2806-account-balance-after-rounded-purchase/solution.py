class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
       
        while purchaseAmount%10>0:
            if purchaseAmount%10 <5:
                purchaseAmount-=1
            else:
                purchaseAmount+=1
        return 100-purchaseAmount
        """
        :type purchaseAmount: int
        :rtype: int
        """
        
