def remove_duplicates(text):
    result=" "
    for ch in text:
        if ch not in result:
            result+=ch
    return result
sentence="programming"
print(remove_duplicates(sentence))
