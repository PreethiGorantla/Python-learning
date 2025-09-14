""" Enums are readable names that are bound to constant value"""

from enum import Enum  
class State(Enum):
    INACTIVE=0
    ACTIVE=1
print(State.ACTIVE)
print(State.ACTIVE.value)
print(State.INACTIVE)
print(State.INACTIVE.value)
print(State['ACTIVE'])
print(State['ACTIVE'].value)
print(list(State))
print(len(State))