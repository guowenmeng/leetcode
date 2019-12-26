class Solution:

    def rob(self,nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        return max(nums[0]+max(self.rob(nums[2:]),self.rob(nums[3:])),nums[1]+max(self.rob(nums[3:]),self.rob(nums[5:])))

    def rob1(self,nums):
        max_1,max_2,max_3=0,0,0
        for i in range(len(nums)):
            max_1, max_2, max_3=max_2,max_3,nums[i]+max(max_1,max_2)
        return max(max_2,max_3)

    def rob2(self, nums):
        last,now=0,0
        for num in nums:
            last,now=now,max(last+num,now)
        return now
if __name__ == '__main__':
    s = Solution()
    l =[1,2,3,1]
    print(s.rob1(l))