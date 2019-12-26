class Solution:
    def maxArea(self, height):
        max_area=0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                max_area=max(max_area,min(height[i]*(j-i),height[j]*(j-i)))
        return max_area

    def maxArea2(self, height):
        left=0
        right=len(height)-1
        result=0
        while left <right:
            water=min(height[left],height[right])*(right-left)
            if water>result:
                result=water
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return result

    def maxArea3(self, height):
        pass

if __name__ == '__main__':
    s=Solution()
    height=[2,3,4,5,18,17,6]
    print(s.maxArea3(height))