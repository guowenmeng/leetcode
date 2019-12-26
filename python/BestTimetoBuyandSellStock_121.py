class Solution:
    def maxProfit(self, prices):
        max_=0
        if len(prices)>0:
            min_=prices[0]
        for i in range(len(prices)):
            if prices[i]<min_:
                min_=prices[i]
            elif prices[i]-min_>max_:
                max_=prices[i]-min_
        return max_

    def maxProfit2(self, prices):
        max_profit,min_price=0,float('inf')
        for price in prices:
            min_price=min(min_price,price)
            max_profit=max(max_profit,price-min_price)
        return max_profit


if __name__ == '__main__':
    s = Solution()
    l =[7,1,5,3,6,4]
    print(s.maxProfit2(l))