class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        total_price = sum([ prices[0], prices[1] ])
        if total_price <= money :
            res = money - total_price
            return res
        else:
            return money 
        