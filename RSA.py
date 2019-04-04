import random
import math
import gen_random
from exponential import exp_mode
from gcd import ext_gcd
import MillerRabin

def gen_prime():
    prime = gen_random.pseudoprime_number()
    flag1 = MillerRabin.millerrabin(prime)
    flag2 = MillerRabin.millerrabin(prime)
    flag3 = MillerRabin.millerrabin(prime)
    if not (flag1 and flag2 and flag3):
        prime = gen_prime()
    '''if MillerRabin.millerrabin(prime) == False:
        prime = gen_prime()'''
    return prime

def gen_key(p, q):
    n = p * q
    euler = (p - 1) * (q - 1)
    e = random.randint(3, euler)
    a = e
    b = euler
    r, x, y = ext_gcd(a, b)
    while r != 1:
        e = random.randint(3, euler)
        a = e
        b = euler
        r, x, y = ext_gcd(a, b)
    print('r', r)
    print('euler', euler)
    print('x', x)
    if x < 0:
        print("x is negative")
        x = x - (x // (b // r)) * (b // r)
        print('x', x)
    d = x
    # error happens when x is negative
    print('n', n, 'e', e, 'd', d)
    return (n, e), (n, d)

def encrypt(m, publickey):
    n = publickey[0]
    e = publickey[1]

    c = exp_mode(m, e, n)
    return c

def decrypt(c, privatekey):
    n = privatekey[0]
    d = privatekey[1]

    m = exp_mode(c, d, n)
    return m

if __name__ == "__main__":
    p = gen_prime()
    print('p', p)
    q = gen_prime()
    print('q', q)
    pubickey, privatekey = gen_key(p, q)
    '''if privatekey[1] < 0:
        print("please retry")'''
    # info = map(ord, "Mathematical Fundation of Information security + 201202001 + 517021910564")
    m = 517021910564123456789456123
    c = encrypt(m, pubickey)
    print('c', c)
    d = decrypt(c, privatekey)
    print('d', d)

