class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        low = 0
        high = l - 1
        if target not in nums:
            return [-1, -1]
        else:
            res = []

            #First Position
            while low <= high:
                mid = (low + high) // 2

                if target == nums[mid]:
                    if len(res) == 0:
                        res.append(mid)
                        high = mid - 1
                    else:
                        if res[0] > mid:
                            res[0] = mid
                            high = mid - 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            #Last Position
            low = 0
            high = l-1
            while low <= high:
                mid = (low + high) // 2

                if target == nums[mid]:
                    if len(res) == 1:
                        res.append(mid)
                        low = mid + 1
                    else:
                        if res[-1] < mid:
                            res[-1] = mid
                            low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return res

            
