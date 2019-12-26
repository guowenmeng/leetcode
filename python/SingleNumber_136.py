class Solution:
    def singleNumber(self, nums):
        dic={}
        for item in nums:
            if item not in dic:
                dic[item]=1
            else:
                dic.pop(item)
        return dic.popitem()[0]

    def singleNumber2(self, nums):
        ans=0
        for num in nums:
            ans^=num
        return ans



if __name__ == '__main__':
    s = Solution()
    l =[2,2,1]
    print(s.singleNumber2(l))