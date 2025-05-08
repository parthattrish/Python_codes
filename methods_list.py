list =["bhalu",7,312,226,7,True,7,None]
print(list)
def appen(lst):
    lst.append(3)
    return lst
def extend(lst):
    lst.extend([3,39])
    return lst
def remove(lst):
    lst.remove(7)
    return lst
def pop(lst):
    lst.pop([2,7])
    return lst
def clear(lst):
    lst.clear()
    return lst
def index(lst):
   return lst.index(7) 
def count(lst):
    lst.count(7)
    return lst
def reverse(lst):
    return lst.reverse
def copy(lst):
    beta=lst.copy()
    return beta
def sorting(lst):
    return lst.sort()
print(index(list))
