class Solution:

    def strStr(self, haystack, needle):
        i=0
        length = len(needle)
        if length==0:
            return 0
        while i <= (len(haystack) - length):
            cur = 0
            while cur <= length - 1:
                if haystack[i + cur] != needle[cur]:
                    break
                else:
                    if cur == length - 1:
                        return i
                    else:
                        cur += 1
            i += 1
        return -1

    def strStr1(self, haystack, needle):
        pass

    def strStr2(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1

if __name__ == '__main__':
    s=Solution()
    haystack="hello"
    needle='ll'
    print(s.strStr(haystack,needle))