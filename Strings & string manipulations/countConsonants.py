def count_consonants(s:str)->int:
    vowels="aeiou"
    s=s.lower()
    return sum(1 for ch in s if ch not in vowels)
text="preethiHanvi"
print(count_consonants(text))