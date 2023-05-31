class Solution(object):
    def twoSum(self, nums, target):
        
        num_checados = dict()
        
        for indice, numero in enumerate(nums):
            necessario = target - nums[indice]
            if necessario in num_checados:
                return [num_checados[necessario], indice]
            num_checados[numero] = indice
        return
            

teste = Solution()
print(teste.twoSum([3,3], 6))