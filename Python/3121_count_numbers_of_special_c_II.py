# Problem: 3121 Count the Number of Special Characters II
# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
#Return the number of special letters in word.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        mayusculas = {}
        minusculas = {}

        for i, c in enumerate(word):
            if c.isupper():
                if c not in mayusculas:
                    mayusculas[c] = i   
            elif c.islower():
                minusculas[c] = i   

        mayusculas_en_minuscula = {c.lower(): i for c, i in mayusculas.items()} 
        claves_comunes = mayusculas_en_minuscula.keys() & minusculas.keys() 
        pares_unicos = {c: minusculas[c] for c in claves_comunes} 

        pares_con_orden = {}

        for letra in pares_unicos:
            idx_minus = minusculas[letra]
            
            letra_mayus = letra.upper()
            idx_mayus = mayusculas[letra_mayus]
            
            if idx_minus < idx_mayus:
                pares_con_orden[letra] = idx_minus

        contador = len(pares_con_orden)
        return contador

word = "cCceDC"
solution = Solution()
result = solution.numberOfSpecialChars(word)
print(result) 