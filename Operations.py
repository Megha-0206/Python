'''def addition(*num):
    sum=0
    for i in num:
        sum+=i
    return sum'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minimun = min(prices)
        day = prices.index(minimun)
        maximum = max(prices)
        Profitable_Day = prices.index(maximum)
        if(Profitable_Day<day):
            prices.remove(maximum)
            maximum = max(prices)
            Profitable_Day = prices.index(maximum)
        else:
            return maximum-minimun
