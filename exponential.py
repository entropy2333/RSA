'''
def Montgeomery(a, b, n):
    reverse = 1
    r = pow(2, n - 1)
    for i in range(1, n + 1):
        if (reverse * r) % n == 1:
            pass
        else:
            reverse += 1
    result = (a * b * reverse) % n
    return result

def exp_mode(base, exponent, n):
    i = exponent - 1
    x = Montgeomery(base, 1 , n)
    while i > 0:
        x = Montgeomery(x, 1, n)
        i -= 1
    return x
print(exp_mode(2, 6, 10000000))
'''
import time
def exp_mode(base, exponent, n):
    bin_array = bin(exponent)[2:][::-1]
    r = len(bin_array)
    base_array = []
    
    pre_base = base
    base_array.append(pre_base)
    
    for _ in range(r - 1):
        next_base = (pre_base * pre_base) % n 
        base_array.append(next_base)
        pre_base = next_base
        
    a_w_b = __multi(base_array, bin_array, n)
    return a_w_b % n

def __multi(array, bin_array, n):
    result = 1
    for index in range(len(array)):
        a = array[index]
        if int(bin_array[index]) == 0:
            continue
        result *= a
        result = result % n # 加快连乘的速度
    return result  
