from random import randint
from math import gcd

def test_ferma(number, base_count):
    print("Тест Ферма для", number) 
    # check number for 10 different bases
    for i in range(base_count):
        #base = randint(2, number - 2)
        base = 22
        if pow(base, number - 1, number) != 1:
            print("основание =", base, "число составное (Ферма)")
            return
        else:
            print("основание =", base, "число, вероятно, простое")
    #print("число, вероятно, простое")
    return

def jacobi(a, n):
    s = 1
    while True:
        if n < 1:
            raise ValueError("Too small module for Jacobi symbol: " + str(n))
        if n & 1 == 0:
            raise ValueError("Jacobi is defined only for odd modules")
        if n == 1:
            return s
        a = a % n
        if a == 0:
            return 0
        if a == 1:
            return s

        if a & 1 == 0:
            if n % 8 in (3, 5):
                s = -s
            a >>= 1
            continue

        if a % 4 == 3 and n % 4 == 3:
            s = -s

        a, n = n, a
    return

def solovay_strassen_test(number, base_count):
    print("Тест Соловэя-Штрассена для", number)
    for i in range(base_count):
        base = randint(2, number - 2)
        
        d = gcd(number, base) 
        if d != 1:
            print("основание =", base, "число составное (НОД)")
        
        # calculate legendre symbol from euler criterion formula  
        y = pow(base, (number - 1) // 2, number)
        x = jacobi(base, number)
        if y != x % number:
            print("основание =", base, "число составное (Якоби)")
            return
        #else:
        #    print("основание =", base, "число, вероятно, простое")
    print("число, вероятно, простое")
    return


def miller_rabin_test(number, count):
    print("Тест Миллера-Рабина для", number)
    s = 0
    r = number - 1
    while r % 2 == 0:
        s = s + 1
        r = r//2
    for i in range(count):
        base = randint(2, number - 2)
        y = pow(base, r, number)
        if y != 1 and y != number - 1:   
            j = 1
            while j <= s - 1 and y != number - 1:
                y = pow(y, 2, number)
                if y == 1:
                    print("основание =", base, "число составное (y = 1)")
                    return
                j = j + 1
            if y != number - 1:
                print("основание =", base, "число составное (y = -1)")
                return
        print("основание =", base, "число, вероятно, простое")
    #print("число, вероятно, простое")
    return


test_ferma(70416887142533176417390411931483993124120785701395296424001, 1)
#solovay_strassen_test(2884167509593581480205474627684686008624483147814647841436801, 5)
#miller_rabin_test(2884167509593581480205474627684686008624483147814647841436801, 5)
#if (2884167509593581480205474627684686008624483147814647841436801-1)%(127-1) == 0: 
#    print("ok!")

#if (70416887142533176417390411931483993124120785701395296424001-1)%(127-1) == 0: 
#    print("ok!")

