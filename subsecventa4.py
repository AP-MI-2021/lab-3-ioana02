def nr_prim(n):
    '''
    functia determina daca un numar este prim sau nu
    :param n numar intreg:
    :return adevarat sau fals:
    '''
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def toate_elementele_prime(lst):
    """
    Determina daca toate numerele dintr-o secventa a listei sunt prime
    :param lst - lista de numere:
    :return adevarat sau fals:
    """
    for x in lst:
        if nr_prim(x) is False:
            return False
    return True


def get_longest_all_primes(lst: list[int]):
    """
    Determina cea mai lunga subsecventa de numere prime
    :param lst - lista de numere:
    :return lista cu cea mai lunga subsecventa de numere prime din lst:
    """
    subsecventa_max1 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if toate_elementele_prime(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventa_max1):
                subsecventa_max1 = lst[i:j + 1]
    return subsecventa_max1


def test_get_longest_all_primes():
    assert get_longest_all_primes([12, 7, 3, 5, 6]) == [7, 3, 5]
    assert get_longest_all_primes([2, 4, 6]) == [2]
    assert get_longest_all_primes([8, 4, 6]) == []




def is_palindrome(n):
    '''
    Verifica daca un numar este palindrom
    :param n: numar intreg
    :return: Retruneaza adevarat daca nr este palindrom si fals in caz contrar
    '''
    if n < 10:
        return False
    rasturnat = 0
    clona = n
    while clona > 0:
        rasturnat = rasturnat * 10 + clona % 10
        clona = clona // 10
    if rasturnat == n:
        return True
    else:
        return False


def palindromelist(l):
    for x in l:
        if is_palindrome(x) is False:
            return False
    return True


def  get_longest_all_palindromes(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa de numere cu proprietatea ca toate nr sunt palindrom
    :param lst: lista cu numere reale
    :return: cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindrom
    '''
    subsecventa_max2 = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if palindromelist(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventa_max2):
                subsecventa_max2 = lst[i:j + 1]
    return subsecventa_max2


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([]) == []
    assert get_longest_all_palindromes([12, 11, 22, 44, 54, 22]) == [11, 22, 44]
    assert get_longest_all_palindromes([12, 11, 22, 44, 54, 22, 66, 101, 202]) == [22, 66, 101, 202]




def toate_elem_pare(lst):
    '''
    determina daca o lista are toate elementele nr pare
    :param lst: lista de nr intregi
    :return: True, daca toate elem din lista sunt nr pare sau False, in caz contrar
    '''
    for i in lst:
        if i % 2 !=0:
            return False
    return True

def test_toate_elem_pare(lst):
    assert toate_elem_pare([1,2,7]) is False
    assert toate_elem_pare([4,6,66,0]) is True
    assert toate_elem_pare([173,9,11,5,39,411]) is False

def get_longest_all_even (lst):
    '''
    determina cea mai lunga subsecventa in care toate elementele sunt numere pare
    :param lst: lista de numere intregi
    :return: cea mai lunga subsecventa in care toate elementele sunt numere pare din lst
    '''
    test_toate_elem_pare(lst)
    subsecventa_max3 = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if toate_elem_pare(lst[i:j+1]) and len(subsecventa_max3) < len(lst[i:j+1]):
                subsecventa_max3 = lst[i:j+1]
    return subsecventa_max3

def test_get_longest_all_even ():
    assert get_longest_all_even([1,3]) == []
    assert get_longest_all_even([2,4,12]) == [2,4,12]
    assert get_longest_all_even([5,90,20,71,10]) == [90,20]




def creare_lista():
    '''
    cream o lista de elemente
    '''
    lst = []
    n= int(input("Dati elementele listei: "))
    for i in range(n):
        lst.append(int(input("l["+ str(i)+ "]=")))
    return lst


def print_menu():
    print("1.citim numerele")
    print("2.afisam cea mai lunga subsecventa de numere prime")
    print("3.afisam cea mai lunga subsecventa de numere palindrom")
    print("4.afisam cea mai lunga subsecventa de numere pare")
    print("5.iesire din program")

def main():
    test_get_longest_all_primes()
    test_get_longest_all_palindromes()
    test_get_longest_all_even()
    lst= []
    while True:
        print_menu()
        optiune= input("Alegeti o optiune: ")
        if optiune== "1":
            l= creare_lista()
        elif optiune== "2":
            print(get_longest_all_primes(l))
        elif optiune== "3":
            print(get_longest_all_palindromes(l))
        elif optiune== "4":
            print(get_longest_all_even(l))
        elif optiune== "5":
            break
        else:
            print("Nu ai ales nicio optiune")

main()