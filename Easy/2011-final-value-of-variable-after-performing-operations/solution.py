class Solution(object):
    def finalValueAfterOperations(self, operations):
        c=0
        for i in operations:
            if i[1]=="-":
                c-=1
            else:
                c+=1
        return c
        """
        :type operations: List[str]
        :rtype: int
        """
        
