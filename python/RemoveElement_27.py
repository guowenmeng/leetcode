class Solution:
    #方法一
    def removeElement(self, nums,val):
        length=len(nums)
        #空
        i = 0
        j = length - 1

        if length==0:
            return 0
        #一个元素
        elif i==j:
            if nums[i]==val:
                return i
            else:
                return i + 1
        # 多个元素
        else:
            while i<j:
                if nums[j] ==val:
                    j-=1
                    continue
                if nums[i]!=val:
                    i+=1
                    continue
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
                i+=1
            #多个且元素都与变量相等
            if i==0 :
                if nums[i]==val:
                    return i
                else:
                    return i+1
            elif i==length-1:
                if nums[i]==val:
                    return i
                else:
                    return i+1
            else:
                if i==j:
                    if nums[i]==val:
                        return i
                    else:
                        return i+1
                if i>j:
                    return i

    # 方法二
    def removeElement2(self, nums, val):
        length=len(nums)
        i,j = 0,length - 1
        while i < j:
            if nums[j]!=val and nums[i]==val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                i += 1
            if nums[j] == val:
                j -= 1
            if nums[i] != val:
                i += 1

        if length==0 or nums[i] == val:
            return i
        else:
            return i + 1



    #方法三
    def removeElement3(self, nums, val):
        i=0
        last=len(nums)-1
        while i<=last:
            if nums[i]==val:
                nums[i],nums[last]=nums[last],nums[i]
                last-=1
            else:
                i+=1

        return last+1

if __name__ == '__main__':
    s=Solution()
    nums=[3,2,2,3]
    val=3
    print(s.removeElement2(nums,val))
