import process
import generate_variable
import constdata

# p=islem.p
# q=islem.q
# e=islem.e
# open_text=islem.open_text

p =int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
e =  int(input("Enter the value of key: "))
open_text =int(input("Enter the value of open text: ")) 

n,n_time,n_text = generate_variable.n_generate(p,q)
phi,phi_time,phi_text = generate_variable.phi_generate(p,q)


if(process.isPrime(p) == False or process.isPrime(q) == False):
    print("p or q is not prime")
elif e < 1 or e > phi:
    print("Invalid key")
else:
    D,d_time,Dtext = generate_variable.generate_secret_key(e,phi)
    cipher_text,cipher_time,cipherText = generate_variable.generate_encrypted_text(open_text,e,n)
    found_open_text,open_time,openText = generate_variable.generate_plain_text(cipher_text,D,n)   
    print("\n")
    print(n_text)
    print(phi_text)
    print(Dtext)
    print(cipherText)
    print(openText)






