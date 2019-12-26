class Solution:
    def generateParenthesis(self, n):
        all=[]
        item=''
        self.findpar(n,n,item,all)
        return all

    def findpar(self,left,right,item,all):
        if left>right:
            return
        if left>0:
            self.findpar(left-1,right,item+'(',all)
        if right>0:
            self.findpar(left,right-1,item+')',all)
        if left==0 and right==0:
            all.append(item)


if __name__ == '__main__':
    s=Solution()
    n=3
    print(s.generateParenthesis(n))