class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j=0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]+nums[i]==target:
                    return [j,i]
        
            
        