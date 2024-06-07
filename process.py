import random


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("No modular inverse, because a and m are not prime between them")
    else:
        return x % m

def isPrime(n, k=5):
    if n <= 3:
        return n == 2 or n == 3
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def format_binary_representation(number):
    binary_representation = bin(number)[2:] 
    length = len(binary_representation)
    formatted_representation = f"{binary_representation}"  
    return formatted_representation

def exponential_operations(text,key,n):
    elements = format_binary_representation(key)[::-1]
    a = 1
    if elements[0] == '1':
        a = text%n
    for i in elements[1:]:
        text **= 2
        text %=n
        if i == '1':
            a*=text
            a%=n
    return a  

def toString(field,value,time):
    return "Field: "+field+",\nValue: "+str(value)+", Time: "+str(time)


    
p =13
q = 17
e = 19
open_text =85