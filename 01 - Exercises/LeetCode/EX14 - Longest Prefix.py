class Solution(object):
    def longestCommonPrefix2(self, strs):
        if not strs:
            return ""

        prefix = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break
        return prefix
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
                i += 1
            prefix = prefix[:i]
            if not prefix:
                break
        return prefix
    

teste = Solution()
print(teste.longestCommonPrefix2(['flower', 'flow', 'fly', 'floght']))