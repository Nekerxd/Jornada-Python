class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        if(x==x[::-1]):return True
        return False


teste = Solution()
print(teste.isPalindrome(1771))
