def string_split(s):
    words= s.split()
    return '-'.join(words)
text="Hello Iam preethi."
b="preethi"
print(string_split(text))
print(string_split(b))


print("-----split-----")
words="hello welcome to python programming"
s=words.split()
print(s)
combine="".join(words)
print(combine)