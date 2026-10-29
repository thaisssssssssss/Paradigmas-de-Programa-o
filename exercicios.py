
def head(list):
    return list[0]

def tail(list):
    return list[1:]

def init(list):
    return list[:-1]

def last(list):
    return list[-1]

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fatorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*fatorial(n-1)

def divisao_fatorial(n):
    if n == 0:
        return 1
    else:
        return divisao_fatorial(n-1) + (1 / fatorial(n))


def somatorio_negativos(list):
    if head(list) == 0:
        return 0
    else:
        if head(list) < 0:
            return head(list) + somatorio_negativos(tail(list))
        else:
            return somatorio_negativos(tail(list))

def conta_negativos(list):
    if head(list) == 0:
        return 0
    else:
        if head(list) < 0:
            return 1 + conta_negativos(tail(list))
        else:
            return conta_negativos(tail(list))

def tamanho_lista(list):
    if head(list) == 0:
        return 1
    else:
        return tamanho_lista(tail(list)) + 1

def primo(n, a):
    if (n-1) == 0:
        return True
    if a % (n-1) == 0:
        return False
    else:
        return primo(n-2, a)
    
    

    
list = [9, -8, -7, -4, -3, -2, 0]
print(tamanho_lista(list))

print(primo(1,1))
