class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=mid=0
        high=len(nums)-1
        for i in range(len(nums)):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
                
            
        