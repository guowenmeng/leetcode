# 动态规划练习

class Solution:
    #方法一：递归
    def minimumTotal(self, triangle):
        return self.findmin(triangle,0,0)

    def findmin(self,triangle,i,j):
        if i ==len(triangle)-1:#递归结束条件
            return triangle[i][j]
        if i<len(triangle)-1 :#递归进行条件
            return min(triangle[i][j]+self.findmin(triangle,i+1,j),triangle[i][j]+self.findmin(triangle,i+1,j+1))
    #方法二：动态规划
    def minimumTotal1(self, triangle):
        for i in range(-2,-len(triangle)-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]



if __name__ == '__main__':
    s=Solution()
    nums=[[2],[3,4],[6,5,7],[4,1,8,3]]
    print(s.minimumTotal1(nums))
