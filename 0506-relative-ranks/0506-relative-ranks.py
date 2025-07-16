class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = []
        l = len(score)
        for i in score:
            arr.append(i)
        arr.sort(reverse=True)

        for i in range(l):
            x = score[i]
            ind = arr.index(x)
            if ind == 0:
                score[i] = "Gold Medal"
            elif ind == 1:
                score[i] = "Silver Medal"
            elif ind == 2:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(ind + 1)
        return score