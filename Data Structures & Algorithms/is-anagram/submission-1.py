class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            st = sorted(s)
            sorted_s="".join(st)
            tt=sorted(t)
            sorted_t="".join(tt)
            if (sorted_s==sorted_t):
                return True
        return False
            