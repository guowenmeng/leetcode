class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur=0
        for i in range(len(nums)):
            if len(nums)==0:
                return 0
            if nums[i]!=nums[cur]:
                cur+=1
                nums[cur]=nums[i]
        return cur+1