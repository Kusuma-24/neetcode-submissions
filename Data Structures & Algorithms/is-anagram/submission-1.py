from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq1 = Counter(s)
        freq2 = Counter(t)

        if len(freq1) != len(freq2):
            return False
            
        for ch , count in freq1.items():
            if freq2[ch] != count:
                return False
        return True

        