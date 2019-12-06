class Solution:
    def searchInsert(self, nums, target):
        start,end=0,len(nums)-1
        while end-start >1:
            i = (start + end) // 2
            if nums[i]==target:
                return i
            elif nums[i]>target:
                end=i
            elif nums[i]<target:
                start=i

        if nums[start]<target and nums[end]>=target:
            return end
        elif nums[start]>=target:
            return start
        elif nums[end]<target:
            return end+1

    def searchInsert2(self, nums, target):
        if target>nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]>=target:
                return i

if __name__ == '__main__':
    s=Solution()
    nums=[1,3,5,6]
    target=2
    print(s.searchInsert2(nums,target))
