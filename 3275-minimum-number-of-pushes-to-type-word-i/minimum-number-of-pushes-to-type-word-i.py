class Solution:
    def minimumPushes(self, s: str) -> int:
        return  [0,8,24,48][n8:=(len(s)//8)] + (n8+1)*(len(s)%8)
        