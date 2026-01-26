class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        ans = 0
        remaining_ones = k
        remaining_rank = n
        for bits in range(50, -1, -1):
            if remaining_ones == 0:
                break

            if bits >= remaining_ones:
                count = comb(bits, remaining_ones)
            else:
                count = 0

            if remaining_rank > count:
                remaining_rank -= count
                ans |= (1 << bits)
                remaining_ones -= 1

        return ans