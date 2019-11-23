# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        # 利用字典求解
        symbol_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        int=0
        for i in range(len(s)):
            if i >0 and symbol_dict[s[i]]>symbol_dict[s[i-1]]:
                int+=symbol_dict[s[i]]-2*symbol_dict[s[i-1]]
            else:
                int+=symbol_dict[s[i]]
        return int


