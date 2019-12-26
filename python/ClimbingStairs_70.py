class Solution:
    #解法一：递归，增加变量计数
    def climbStairs(self, n):
        step=0
        count = 0
        count=self.findway(n,step,count)
        return count


    def findway(self,n,step,count):
        if step==n-2:
            count+=2
            return count
        if step==n-1:
            count+=1
            return count
        count=self.findway(n,step+1,count)
        count=self.findway(n,step+2,count)
        return count

    #方法二：视频教程的解法
    def climbStairs1(self, n):
        prev,current=0,1
        for i in range(n):
            prev,current=current,prev+current
        return current

    #方法三：官方暴力
    def climbStairs2(self, n):
        step = 0
        count = self.findway2(n, step)
        return count

    def findway2(self, n, step):
        if step == n:
            return 1
        if step>n:
            return 0
        return self.findway2(n, step + 1)+self.findway2(n, step + 2)

    def climbStairs3(self, n):
        count1=1
        count2=2
        if n==2:
            return count2
        if n==1:
            return count1
        for i in range(3,n+1,1):
            count=count1+count2
            count1=count2
            count2=count
        return count





if __name__ == '__main__':
    s=Solution()
    n=1
    print(s.climbStairs3(n))