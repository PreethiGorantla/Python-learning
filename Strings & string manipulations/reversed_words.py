def reversed_word(sentence):
    words=sentence.split()
    reversed_words=[words[::-1] for word in words]
    return reversed_words
sentence="python programming"
print(reversed_word(sentence))
