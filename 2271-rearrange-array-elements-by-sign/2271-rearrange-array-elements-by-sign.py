class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        p=0
        n=1
        t=[0]*len(nums)
        if len(nums)==1:
            return nums
        for i in range(len(nums)):
            if nums[i]<0:
                t[n]=nums[i]
                n+=2
            else:
                t[p]=nums[i]
                p+=2
        return t


        