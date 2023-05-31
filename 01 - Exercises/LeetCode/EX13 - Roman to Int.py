class Solution(object):
    def romanToInt(self, s):
        
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        resultado = 0
        
        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                resultado -= roman[a]
            else:
                resultado += roman[a]
        return resultado + roman[s[-1]]
    
teste = Solution()
print(teste.romanToInt("MCMXCIV"))
        