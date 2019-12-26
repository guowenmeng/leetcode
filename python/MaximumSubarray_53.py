class Solution:
    def maxSubArray(self, nums):
        max_sum=max(nums)
        if max_sum<0:
            return max_sum
        for i in range(0,len(nums)):
            if nums[i]<0:
                continue
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum<0:
                    break
                elif sum>max_sum:
                    max_sum=sum

        return max_sum

    def maxSubArray1(self, nums):
        if max(nums)<0:
            return max(nums)
        local_max,global_max=0,0
        for num in nums:
            local_max=max(0,local_max+num)
            global_max=max(global_max,local_max)
        return global_max



if __name__ == '__main__':
    s=Solution()
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))