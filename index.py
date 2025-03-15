
# Desafio de Programação: Contar Números Pares em um Array
def pares(*numbers):
     for number in numbers:
             if number % 2 == 0:
              print(number)

pares(1, 2, 3, 4,20, 40,22,21,42,41)

# Desafio de Progamação: Two sum
nums = [2,4,5,6,2]
target = 10
def twoSum( nums, target):
       visto = {}
       for i in range(len(nums)):
          resultado = target - nums[i]
          if resultado in visto:
            return[i, visto[resultado]]
          visto[nums[i]] = i
       return []

print(twoSum( nums, target))