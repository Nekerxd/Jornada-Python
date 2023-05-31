class Solution(object):
    def romanToInt(self, s):
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        resultado = 0
        for indice, letra in enumerate(s):
            if indice < len(s) - 1 and roman[letra] < roman[s[indice + 1]]:resultado -= roman[letra]
            else:resultado += roman[letra]
        return resultado
    
teste = Solution()
print(teste.romanToInt("MCMXCIV"))
        