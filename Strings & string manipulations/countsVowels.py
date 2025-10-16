def is_vowel(s:str) ->int:
    vowels="aeiou"
    s=s.lower()
    return sum(1 for ch in s if ch in vowels)
text="preethi"
print(is_vowel(text))