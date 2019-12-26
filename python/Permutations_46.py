class Solution:
    def permute(self, nums):
        all=[]
        item=[]
        self.findper(nums,item,all)
        return all



    def findper(self,nums,item,all):
        if len(nums)==0:
            all.append(item)
            return all
        else:
            for i,e in enumerate(nums):
                self.findper(nums[:i]+nums[i+1:],item+[e],all)

    def permute1(self,nums):
        if len(nums)<=1:
            return [nums]

        answer=[]
        for i,num in enumerate(nums):
            n=nums[:i]+nums[i+1:]
            for y in self.permute1(n):
                answer.append([num]+y)
        return answer


if __name__ == '__main__':
    s=Solution()
    n=[1,2,3]
    print(s.permute1(n))