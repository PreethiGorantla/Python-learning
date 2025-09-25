# strings are written with in quotes (" " or ' ' )
"python"
"is a hign level language"
language ="python"
language+=" is a high level language"
print(language)


#multiple line string
print(""" Machine Learning
      

      allows computers
      

      to learn from the data""")


#methods
name ="Vignan Foundation For Science,Technology and Research"
print(name.lower())
print(name.islower())
print(name.upper())
print(name.isupper())
print(name.title()) # prints 1st letter of every word is capital
print(name.startswith("preethi"))
print(name.endswith("hello"))
print(name.replace("Vignan Foundation For Science,Technology and Research","VFSTR"))
print(name)
print(name.split())
print(name.strip())
print(name.join("university"))
print(name.find("For"))
print(name.isalpha())
print(name.isalnum())
print(name.isdecimal())
print(len(name))
print("Foundation" in name)
print(name[9])
print(name[-2])
print(name.replace("V","z"))


