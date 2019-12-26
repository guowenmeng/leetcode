class Solution:
    def majorityElement(self, nums):
        index,cnt=0,1
        for i in range(1,len(nums)):
            if nums[index]==nums[i]:
                cnt+=1
            else:
                cnt-=1
                if cnt==0:
                    index=i
                    cnt=1
        return nums[index]
    #排序法
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]

    #分治法
    def majorityElement2(self, nums):
        pass

    

if __name__ == '__main__':
    s = Solution()
    l =[3,2,3]
    print(s.majorityElement1(l))