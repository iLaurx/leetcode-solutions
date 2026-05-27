# Problem: 3120
# The time Complexity is O(n)
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        mayusculas = set(c for c in word if c.isupper())  # {'A', 'B', 'C'}
        minusculas = set(c for c in word if c.islower())  # {'a', 'b', 'c'}

        mayusculas_en_minuscula = set(c.lower() for c in mayusculas)  # {'a', 'b', 'c'}

        pares_unicos = mayusculas_en_minuscula & minusculas  # {'a', 'b', 'c'}

        contador = len(pares_unicos)

        return contador

solution = Solution()
result = solution.numberOfSpecialChars("aaAbcBC")
print(result)

# The time Complexity of the brute force solution is O(n^2)

#! Brute Force 
word = "aaAbcBC"

contador = 0
n = len(word)
visitados = set()
for i in range(n): 
    first = word[i]

    if first.lower() in visitados:
        continue

    for j in range(i + 1, n):
        second = word[j]

        if (ord(first) - ord(second) == 32 or (ord(first) - ord(second) == -32)):
            contador += 1

            visitados.add(first.lower())
            break
print(contador)