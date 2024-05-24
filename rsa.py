import islem
import degiskenuret
import constdata

# p=islem.p
# q=islem.q
# e=islem.e
# open_text=islem.open_text

p =int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
e =  int(input("Enter the value of key: "))
open_text =int(input("Enter the value of open text: ")) 

n,n_time,n_text = degiskenuret.n_uret(p,q)
phi,phi_time,phi_text = degiskenuret.phi_uret(p,q)


if(islem.isPrime(p) == False or islem.isPrime(q) == False):
    print("p or q is not prime")
elif e < 1 or e > phi:
    print("Invalid key")
else:
    D,d_time,Dtext = degiskenuret.gizli_anahtar_uret(e,phi)
    cipher_text,cipher_time,cipherText = degiskenuret.sifreli_metin_uret(open_text,e,n)
    found_open_text,open_time,openText = degiskenuret.acik_metin_uret(cipher_text,D,n)   
    print("\n")
    print(n_text)
    print(phi_text)
    print(Dtext)
    print(cipherText)
    print(openText)






