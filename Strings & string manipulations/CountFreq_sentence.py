def freq_count(sentence):
    sentence=sentence.lower()
    import string
    sentence=sentence.translate(str.maketrans("","",string.punctuation))
    """str.maketrans("","",string.punctuation) creates a translation table
       that removes all punctuations."""
    words=sentence.split()
    freq={} #dictionary to stores the words with frequency
    for word in words:
        freq[word]=freq.get(word,0)+1 #returns current count(default by 0 if not present) and increment by 1.
    return freq
sentence="Machine learning is making the computers to learn from the data and make the predictions using data."
print(freq_count(sentence))