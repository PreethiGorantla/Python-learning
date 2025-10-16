def longest_word(sentence):
    words=sentence.split()
    longest=max(words,key=len)
    return longest
sentence="welcome to python programming"
print(longest_word(sentence))


print("-------------------another method---------------------------")
import re
def longest(word):
    words=re.findall(r"[A-Za-z]+",sentence)
    if not words:
        return None
    word=max(words,key=len)
    return word,len(word)
sen="machine learning is about predicting future outcomes."
print(longest(sen))