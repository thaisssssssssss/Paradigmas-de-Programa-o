
def head(list):
    return list[0]

def tail(list):
    return list[1:]

def init(list):
    return list[:-1]

def last(list):
    return list[-1]

def concatena(list1, list2):
    if not list1:
        return list2
    else:
        return concatena(tail(list1), list2 + [head(list1)])

def pertence(list, n):
    if not list:
        return False
    else:
        if (head(list) == n):
            return True
        else:
            return pertence(tail(list), n)

def concatena_diferentes(list1, list2):
    if not list1:
        return list2
    else:
        if(not pertence(list2, head(list1))):
            return concatena_diferentes(tail(list1), list2 + [head(list1)])
        else:
            return concatena_diferentes(tail(list1), list2)


list2 = [1, 2, 3, 4, 5]
list1 = [4, 5, 6, 5, 7]
#print(pertence(list1, 9))
list = concatena_diferentes(list1, list2)
print(list)
