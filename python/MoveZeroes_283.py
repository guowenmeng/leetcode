class Solution:
    def moveZeroes(self, nums):
        i,j=0,1
        length=len(nums)
        while i<length-1 and j <=length-1:
            if nums[i]!=0:
                i+=1
                j+=1
                continue
            if nums[j]==0:
                j+=1
                continue
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
        print(nums)

    def moveZeroes1(self,nums):
        pos=0
        for i in renge(len(nums)):
            if nums[i]:
                nums[pos]=nums[i]
                pos+=1
        for i in range(pos,len(nums)):
            nums[i]=0


if __name__ == '__main__':
    s = Solution()
    l =[0,1,0,0,3,12]
    print(s.moveZeroes(l))