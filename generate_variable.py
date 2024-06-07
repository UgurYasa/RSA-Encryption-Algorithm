import process
import time

def n_generate(p,q):
    start = time.time()
    n = p * q
    end = time.time()
    n_time = end - start
    text = process.toString("(N)",n,n_time)
    return n,n_time,text

def phi_generate(p,q):
    start = time.time()
    phi=(p-1) * (q-1)
    end = time.time()
    phi_time = end - start
    text = process.toString("Q(n)",phi,phi_time)
    return phi,phi_time,text

def generate_secret_key(e,phi):
    d_start = time.time()
    D = process.mod_inverse(e, phi)
    d_end = time.time()
    d_time = d_end - d_start
    text = process.toString("Gizli Anahtar (D)",D,d_time)
    return D,d_time,text

def generate_encrypted_text(open_text,e,n):
    start= time.time()
    cipher_text = process.exponential_operations(open_text,e,n)
    end = time.time()
    cipher_time = end - start
    text = process.toString("Şifreleme",cipher_text,cipher_time)
    return cipher_text,cipher_time,text

def generate_plain_text(cipher_text,D,n):
    start = time.time()
    found_open_text = process.exponential_operations(cipher_text,D,n)
    end = time.time()
    open_time = end - start
    text = process.toString("Deşifreleme",found_open_text,open_time)
    return found_open_text,open_time,text

