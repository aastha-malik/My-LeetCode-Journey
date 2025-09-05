class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = len(s1)
        
        s1_counter = Counter(s1)
        window_counter = Counter(s2[:l])

        if s1_counter == window_counter:
            return True
        
        for i in range(l, len(s2)):
            left_ind = i - l
            right_ind = i
            
            window_counter[s2[left_ind]] -= 1
            window_counter[s2[right_ind]] += 1

            if s1_counter == window_counter:
                return True
        return False

        