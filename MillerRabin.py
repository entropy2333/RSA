import random
from exponential import exp_mode
def millerrabin(n):

    # caculate m & a
    a = 0
    tmp1 = 1
    tmp2 = n - 1
    while tmp2 % 2 == 0:
        a += 1
        tmp1 *= 2
        tmp2 = tmp2 // 2
        # print(a, tmp1, tmp2)
    m = (n - 1) // tmp1
    # print (a, m)

    # caculate b**m % n by Montgeomery
    b = random.randint(2,10)
    x = exp_mode(b, m, n)
    # print(b, x)

    flag = True
    i = 1
    while x != (n - 1):
        if i == a:
            flag = False
            break
        else:
            x = (x * x) % n
            i += 1
    
    if flag == True:
        print("millerrabin isprime")
    else:
        print("millerrabin isnotprime")
    return flag

