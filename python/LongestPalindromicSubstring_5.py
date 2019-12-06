class Solution:
    def longestPalindrome(self, s):
        # if len(s)==1:
        #     return s
        max_length=1
        start=0
        for i in range(0,len(s)-1):
            left, right = i - 1, i + 1
            while left>=0 and right<=len(s)-1:
                if s[left]==s[right]:
                    left-=1
                    right+=1
                else:
                    break
            if right-left-1>max_length:
                max_length=right-left-1
                start=left+1
            if s[i+1]==s[i]:
                left,right=i-1,i+2
                while left>=0 and right<=len(s)-1:
                    if s[left]==s[right]:
                        left-=1
                        right+=1
                    else:
                        break
                if right-left-1>max_length:
                    max_length=right-left-1
                    start=left+1
        return s[start:start+max_length]

    def longestPalindrome2(self, s):
        max_length,start=1,0
        for i in range(0, len(s) - 1):
            max_i,start_i=self.getmaxlength(s,i)
            if max_i > max_length:
                max_length,start= max_i,start_i
        return s[start:start + max_length]

    def getmaxlength(self,s,i):
        left,right=i-1,i+1
        while left>=0 and right<=len(s)-1:
            if s[left] == s[right]:
                left-=1
                right += 1
            else:
                break
        max_length = right - left - 1
        start = left + 1
        if s[i + 1] == s[i]:
            left, right = i - 1, i + 2
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            if right - left - 1 > max_length:
                max_length = right - left - 1
                start = left + 1

        return max_length,start

    def longestPalindrome3(self, s):
        palindrome=''
        for i in range(len(s)):
            len1=len(self.getlongestpalindrome(s,i,i))
            if len1>len(palindrome):
                palindrome=self.getlongestpalindrome(s,i,i)
            len2=len(self.getlongestpalindrome(s,i,i+1))
            if len2>len(palindrome):
                palindrome=self.getlongestpalindrome(s,i,i+1)
        return palindrome

    def getlongestpalindrome(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]


if __name__ == '__main__':
    so=Solution()
    s="bbbb"
    print(so.longestPalindrome3(s))


