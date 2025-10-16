text="Data Science is about predicting future outcomes"
substring="Predicting"


if substring.casefold() in text.casefold():
    print(f"{substring} is in text")
else:
     print(f"{substring} not found in text")

