import islem
import time

def n_uret(p,q):
    start = time.time()
    n = p * q
    end = time.time()
    n_time = end - start
    text = islem.toString("(N)",n,n_time)
    return n,n_time,text

def phi_uret(p,q):
    start = time.time()
    phi=(p-1) * (q-1)
    end = time.time()
    phi_time = end - start
    text = islem.toString("Q(n)",phi,phi_time)
    return phi,phi_time,text

def gizli_anahtar_uret(e,phi):
    d_start = time.time()
    D = islem.mod_inverse(e, phi)
    d_end = time.time()
    d_time = d_end - d_start
    text = islem.toString("Gizli Anahtar (D)",D,d_time)
    return D,d_time,text

def sifreli_metin_uret(open_text,e,n):
    start= time.time()
    cipher_text = islem.modalmayacalisiyorum(open_text,e,n)
    end = time.time()
    cipher_time = end - start
    text = islem.toString("Şifreleme",cipher_text,cipher_time)
    return cipher_text,cipher_time,text

def acik_metin_uret(cipher_text,D,n):
    start = time.time()
    found_open_text = islem.modalmayacalisiyorum(cipher_text,D,n)
    end = time.time()
    open_time = end - start
    text = islem.toString("Deşifreleme",found_open_text,open_time)
    return found_open_text,open_time,text

