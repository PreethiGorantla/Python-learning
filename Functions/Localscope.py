#Local scopes cannot uses variable in other local scope

def spam():
    eggs=101
    name="hen"
    print(eggs)

def ham():
    dish="puri"
    eggs=0

spam()
