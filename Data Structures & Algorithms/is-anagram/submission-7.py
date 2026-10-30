class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        sum_s = {}
        sum_t = {}
        for i in range(len(s)):
            sum_s[s[i]] = sum_s.get(s[i] , 0) + 1 
            sum_t[t[i]] = sum_t.get(t[i] , 0) + 1
        return sum_s == sum_t
