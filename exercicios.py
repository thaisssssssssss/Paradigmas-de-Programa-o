# Questao 1
def head(list):
    return list[0]

# Questao 2
def tail(list):
    return list[1:]

# Questao 3
def init(list):
    return list[:-1]

# Questao 4
def last(list):
    return list[-1]

# Questao 5
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# Questao 6
def fatorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*fatorial(n-1)

# Questao 7
def divisao_fatorial(n):
    if n == 0:
        return 1
    else:
        return divisao_fatorial(n-1) + (1 / fatorial(n))

# Questao 8.1
def somatorio_negativos(list):
    if head(list) == 0:
        return 0
    else:
        if head(list) < 0:
            return head(list) + somatorio_negativos(tail(list))
        else:
            return somatorio_negativos(tail(list))

# Questao 8.2 (com lista vazia)
def sn(list):
    if not list:
        return 0
    else:
        if head(list) < 0:
            return head(list) + sn(tail(list))
        else:
            return sn(tail(list))

# Questao 9.1
def conta_negativos(list):
    if head(list) == 0:
        return 0
    else:
        if head(list) < 0:
            return 1 + conta_negativos(tail(list))
        else:
            return conta_negativos(tail(list))

# Questao 9.2 (com lista vazia)
def cn(list):
    if not list:
        return 0
    else:
        if head(list) < 0:
            return 1 + cn(tail(list))
        else:
            return cn(tail(list))

# Questao 10.1
def tamanho_lista(list):
    if head(list) == 0:
        return 1
    else:
        return tamanho_lista(tail(list)) + 1

# Questao 10.2
def tam(list):
    if not list:
        return 0
    else:
        return 1 + tam(tail(list))

# Questao 11
def primo(n):
    return p(n, n)

# Questao 11 (auxiliar)
def p(n, a):
    if(a < 2):
        return False
    else:
        if(n == 2):
            return True
        elif(a % (n-1) == 0):
            return False
        else:
            return p(n-1, a)

# Questao 12
def lista_primos(n):
    list = []
    contador = 0
    if n == 0:
        return list
    else:
        return aux_lista_primos(list, contador, n)

# Questao 12 (auxiliar)
def aux_lista_primos(list, contador, n):
    if tam(list) == n:
        return list
    else:
        if primo(contador) == True:
            return aux_lista_primos(list + [contador], contador + 1, n)
        else:
            return aux_lista_primos(list, contador + 1, n)

# Questao 13
def concatena(list1, list2):
    if not list1:
        return list2
    else:
        return [head(list1)] + concatena(tail(list1), list2)

# Questao 14.1
def pertence(list, elemento):
    if(head(list) == 0):
        return False
    else:
        if(head(list) == elemento):
            return True
        else:
            return pertence(tail(list), elemento)

# Questao 14.2
def per(list, n):
    if not list:
        return False
    else:
        if head(list) == n:
            return True
        else:
            return per(tail(list), n)

# Questao 15.1 (minha, porem permite replicas internas, meu simbolo de + e uniao esta confuso tbm)
def uniao(list1, list2):
    if not list1:
        return list2
    else:
        if not per(list2, head(list1)):
            return uniao(tail(list1), list2 + [head(list1)])
        else:
            return uniao(tail(list1), list2)

# Questao 15.2 (IA, nao permite repeticoes)
def uniao(list1, list2):
    if not list1:
        if not list2:
            return []
        elif per(tail(list2), head(list2)):
            return uniao([], tail(list2))
        else:
            return [head(list2)] + uniao([], tail(list2))

    elif per(list2, head(list1)) or per(tail(list1), head(list1)):
        return uniao(tail(list1), list2)

    else:
        return [head(list1)] + uniao(tail(list1), list2)

    
# Questao 16.1
def maiores_n(list, n):
    if(head(list) == 0):
        return 0
    else:
        if(head(list) > n):
            return 1 + maiores_n(tail(list), n)
        else:
            return maiores_n(tail(list), n)
    
# Questao 16.2
def maiores(list, n):
    if not list:
        return 0
    else:
        if head(list) > n:
            return 1 + maiores(tail(list), n)
        else:
            return maiores(tail(list), n)

# Questao 17
def lista_maiores_n(list, n):
    list_final = []
    return lista_maiores_n_aux(list_final, list, n)

# Questao 17 (auxiliar)
def lista_maiores_n_aux(list_final, list, n):
    if not list:
        return list_final
    else:
        if head(list) > n:
            return lista_maiores_n_aux(concatena(list_final, [head(list)]), tail(list), n)
        else:
            return lista_maiores_n_aux(list_final, tail(list), n)

# Questao 18
def inverte_lista(list):
    list_inverted = []
    return inverte_lista_aux(list_inverted, list)
    
# Questao 18 (auxiliar)
def inverte_lista_aux(list_inverted, list):
    if not list:
        return list_inverted
    else:
        return inverte_lista_aux(concatena([head(list)], list_inverted), tail(list))

# Questao 19
def palindromo(list):
    return concatena(list, inverte_lista(list))

# Questao 20
def strip(list1, list2):
    if not list1:
        return list2
    else:
        return strip(tail(list1), strip_aux(head(list1), list2))

# Questao 20 (auxiliar)
def strip_aux(a, list):
    if not list:
        return list
    else:
        if a == head(list):
            return strip_aux(a, tail(list))
        else:
            return concatena([head(list)], strip_aux(a, tail(list)))

# Questao 21
def consoant_list(l1, l):
    if not l1:
        if not l: 
            return True
        else:
            return False
    else:
        c_list = strip(["a","e","i","o","u"], l)
        print("c:", c_list)
        if c_list == l1:
            return True
        else:
            return False

list = [9, -8, -7, -4, -3, -2, 0]
list1 = [7, 0, -8]

print("soma negativos 8.1:", somatorio_negativos(list))
print("soma negativos 8.2:", sn(list))
print("conta negativos 9.1:", conta_negativos(list))
print("soma negativos 9.2:", cn(list))
print("tamanho lista 10.1:", tamanho_lista(list))
print("tamanho lista 10.2:", tam(list))
print("pertence lista 14.1:", pertence(list, 7))
print("pertence lista 14.1:", per(list, 7))
print("primo:", primo(9))
print("maiores que n:", maiores(list, -1))
print("lista primos", lista_primos(8))
print("lista maiores n:", lista_maiores_n(list, -3))
print("lista invertida:", inverte_lista(list))
print("palindromo:", palindromo(list))
print("stripo aux", strip_aux(-3, list))
print("strip:", strip(list1, list))
print("consoant list:", consoant_list(["s", "d", "d"], ["s", "d", "d"]))
list1 = [3, 5, 6]
list2 = [9, 8, 7, 6]
print("concatena:", concatena(list1, list2))
print("uniao:", uniao(list1, list2))
print("list1:", list1)
print("list2:", list2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fat(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fat(n-1)

# print("fibonnaci:", fib(8))
# print("fatorial:", fat(7))
